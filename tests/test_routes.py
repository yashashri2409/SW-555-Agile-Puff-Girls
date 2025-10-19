import pytest
from models import Habit


# === Habit Tracker Tests ===


def test_habit_tracker_get_returns_ok(logged_in_client):
    """Test that GET /habit-tracker returns a 200 status code when authenticated."""
    # Act
    response = logged_in_client.get('/habit-tracker')

    # Assert
    assert response.status_code == 200


def test_habit_tracker_post_creates_habit(logged_in_client, app):
    """Test that POST /habit-tracker creates a new habit in the database when authenticated."""
    # Arrange
    habit_data = {'name': 'Read 20 pages', 'description': 'Daily reading goal'}

    # Act
    response = logged_in_client.post('/habit-tracker', data=habit_data, follow_redirects=False)

    # Assert
    assert response.status_code == 302
 
    with app.app_context():
        stored = Habit.query.filter_by(name='Read 20 pages').first()
        assert stored is not None
        assert stored.description == 'Daily reading goal'


# === Parametrized Tests ===


@pytest.mark.parametrize(
    "endpoint",
    ["/habit-tracker"]
)
def test_all_modules_get_returns_ok(logged_in_client, endpoint):
    """Test that all module endpoints return 200 status code on GET requests when authenticated."""
    # Act
    response = logged_in_client.get(endpoint)

    # Assert
    assert response.status_code == 200