"""
Pytest configuration and fixtures for testing.

This module provides shared fixtures used across all test files:
- app: Flask application instance with test configuration
- client: Flask test client for making HTTP requests
"""

import pytest

from app import app as flask_app
from app import otp_store
from extensions import db


@pytest.fixture
def app(tmp_path):
    """
    Create and configure a Flask application instance for testing.

    Uses a temporary SQLite database that is created fresh for each test
    and cleaned up after the test completes.

    Args:
        tmp_path: pytest fixture providing a temporary directory path

    Yields:
        Flask application configured for testing
    """
    db_path = tmp_path / "test.db"
    flask_app.config.update(
        TESTING=True,
        SQLALCHEMY_DATABASE_URI=f"sqlite:///{db_path}",
        SQLALCHEMY_ENGINE_OPTIONS={"connect_args": {"check_same_thread": False}},
    )

    with flask_app.app_context():
        db.session.remove()
        db.drop_all()
        db.create_all()
        otp_store.clear()
        yield flask_app
        otp_store.clear()
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    """
    Create a Flask test client for making HTTP requests in tests.

    Args:
        app: Flask application fixture

    Returns:
        Flask test client instance
    """
    return app.test_client()


@pytest.fixture
def logged_in_client(client):
    """
    Create a Flask test client with a simulated authenticated session.

    This client can be used to test routes protected by session authentication.

    Args:
        client: Flask test client fixture

    Returns:
        Flask test client with an authenticated session
    """
    with client.session_transaction() as sess:
        # Simulate a successful sign-in required by habit-tracker route
        sess["authenticated"] = True
        sess["email"] = "test@example.com"
    return client
