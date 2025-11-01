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


def test_habit_tracker_delete_removes_habit(client, app):
    """Test that POST /habit-tracker/delete/<id> removes a habit from the database."""
    # Arrange
    with app.app_context():
        habit = Habit(name='Morning Run', description='Run 5k every morning')
        from extensions import db
        db.session.add(habit)
        db.session.commit()
        habit_id = habit.id

    # Act
    response = client.post(f'/habit-tracker/delete/{habit_id}', follow_redirects=False)

    # Assert
    assert response.status_code == 302
    assert response.location == '/habit-tracker'
    with app.app_context():
        deleted_habit = Habit.query.filter_by(id=habit_id).first()
        assert deleted_habit is None


def test_habit_tracker_delete_invalid_id_returns_404(client):
    """Test that POST /habit-tracker/delete/<invalid_id> returns 404."""
    # Act
    response = client.post('/habit-tracker/delete/99999', follow_redirects=False)

    # Assert
    assert response.status_code == 404


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

# === Mark Habit as Complete Tests ===

def test_habit_mark_complete_updates_status(logged_in_client, app):
    """Test that marking a habit as complete updates its completion status in the database."""
    from extensions import db
    from models import Habit

    # Arrange – create a habit first
    with app.app_context():
        habit = Habit(name='Drink Water', description='8 glasses per day', completed=False)
        db.session.add(habit)
        db.session.commit()
        habit_id = habit.id

    # Act – call the mark-complete route
    response = logged_in_client.post(f'/habit-tracker/complete/{habit_id}', follow_redirects=False)

    # Assert – check response and DB state
    assert response.status_code == 302  # redirect after marking complete
    with app.app_context():
        updated_habit = Habit.query.get(habit_id)
        assert updated_habit.completed is True


def test_habit_mark_complete_invalid_id_returns_404(logged_in_client):
    """Test that marking a non-existent habit returns 404."""
    response = logged_in_client.post('/habit-tracker/complete/99999', follow_redirects=False)
    assert response.status_code == 404
