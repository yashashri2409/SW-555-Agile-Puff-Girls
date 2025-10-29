import pytest
from flask import url_for


def test_theme_toggle_endpoint_exists(client):
    """Test that the theme toggle endpoint exists and returns 200."""
    response = client.get("/theme/settings")
    assert response.status_code == 200


def test_theme_toggle_saves_preference(client):
    """Test that toggling theme saves the preference."""
    response = client.post("/theme/toggle", json={"theme": "dark"})
    assert response.status_code == 200
    assert response.json["success"] is True
    assert response.json["theme"] == "dark"


def test_theme_preference_persists(client):
    """Test that theme preference is remembered between requests."""
    # Set preference
    client.post("/theme/toggle", json={"theme": "dark"})

    # Check if preference is remembered
    response = client.get("/theme/settings")
    assert response.json["theme"] == "dark"


def test_invalid_theme_handled(client):
    """Test that invalid theme values are handled gracefully."""
    response = client.post("/theme/toggle", json={"theme": "invalid"})
    assert response.status_code == 400
    assert "error" in response.json
