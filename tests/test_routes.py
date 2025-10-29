import pytest

from app import otp_store
from models import Habit

# === Habit Tracker Tests ===

# === Sign-in and Auth Tests (User Story 01) ===


def test_signin_get_returns_ok(client):
    """Test that the GET /signin page loads successfully."""
    response = client.get("/signin")
    assert response.status_code == 200


def test_otp_generation_success(client):
    """Test that posting an email to /signin generates a 6-digit OTP."""
    # Arrange
    email = "test@example.com"
    data = {"email": email}

    # Act
    response = client.post("/signin", json=data)

    # Assert
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data["success"]
    assert "otp" in json_data
    assert len(json_data["otp"]) == 6
    assert otp_store.get(email) == json_data["otp"]  # Check global store


def test_otp_verification_success(client):
    """Test successful OTP verification logs the user in and clears the OTP."""
    # Arrange: Request and store OTP first
    email = "success@example.com"
    client.post("/signin", json={"email": email})
    otp = otp_store.get(email)  # Get the generated OTP

    # Act: Verify the OTP
    data_verify = {"email": email, "otp": otp, "action": "verify"}
    response_verify = client.post("/signin", json=data_verify)

    # Assert
    assert response_verify.status_code == 200
    json_data = response_verify.get_json()
    assert json_data["success"]

    # Verify session and OTP store cleanup
    with client.session_transaction() as sess:
        assert sess.get("authenticated")
        assert sess.get("email") == email
    assert email not in otp_store  # OTP should be consumed and deleted


def test_otp_verification_failure_invalid_otp(client):
    """Test failed OTP verification with an incorrect OTP."""
    # Arrange: Request and store OTP first
    email = "failure@example.com"
    client.post("/signin", json={"email": email})

    # Act: Verify with incorrect OTP
    data_verify = {"email": email, "otp": "000000", "action": "verify"}
    response_verify = client.post("/signin", json=data_verify)

    # Assert
    assert response_verify.status_code == 200
    json_data = response_verify.get_json()
    assert not json_data["success"]
    assert "Invalid OTP" in json_data["message"]

    # Verify no session was set and OTP is still in store
    with client.session_transaction() as sess:
        assert sess.get("authenticated") is None
    assert email in otp_store  # Failed attempt should NOT clear the OTP


def test_logout_clears_session(client):
    """Test that the /logout route clears the session and redirects to home."""
    # Arrange: Simulate login
    with client.session_transaction() as sess:
        sess["authenticated"] = True
        sess["email"] = "logout_test@example.com"

    # Act
    response = client.get("/logout", follow_redirects=False)

    # Assert
    assert response.status_code == 302
    assert response.location == "/"

    # Check session after redirect
    with client.session_transaction() as sess:
        assert sess.get("authenticated") is None
        assert sess.get("email") is None


def test_habit_tracker_requires_auth_unauthenticated(client):
    """Test that access to /habit-tracker without authentication redirects to /signin."""
    # Act
    response = client.get("/habit-tracker", follow_redirects=False)

    # Assert
    assert response.status_code == 302  # Redirect expected
    assert response.location == "/signin"  # Redirects to signin


# === Basic CRUD Tests ===


def test_habit_tracker_get_returns_ok(logged_in_client):
    """Test that GET /habit-tracker returns a 200 status code when authenticated."""
    # Act
    response = logged_in_client.get("/habit-tracker")

    # Assert
    assert response.status_code == 200


def test_habit_tracker_post_creates_habit(logged_in_client, app):
    """Test that POST /habit-tracker creates a new habit in the database when authenticated."""
    # Arrange
    habit_data = {"name": "Read 20 pages", "description": "Daily reading goal"}

    # Act
    response = logged_in_client.post("/habit-tracker", data=habit_data, follow_redirects=False)

    # Assert
    assert response.status_code == 302

    with app.app_context():
        stored = Habit.query.filter_by(name="Read 20 pages").first()
        assert stored is not None
        assert stored.description == "Daily reading goal"


def test_habit_tracker_delete_removes_habit(client, app):
    """Test that POST /habit-tracker/delete/<id> removes a habit from the database."""
    # Arrange
    with app.app_context():
        habit = Habit(name="Morning Run", description="Run 5k every morning")
        from extensions import db

        db.session.add(habit)
        db.session.commit()
        habit_id = habit.id

    # Act
    response = client.post(f"/habit-tracker/delete/{habit_id}", follow_redirects=False)

    # Assert
    assert response.status_code == 302
    assert response.location == "/habit-tracker"
    with app.app_context():
        deleted_habit = Habit.query.filter_by(id=habit_id).first()
        assert deleted_habit is None


def test_habit_tracker_delete_invalid_id_returns_404(client):
    """Test that POST /habit-tracker/delete/<invalid_id> returns 404."""
    # Act
    response = client.post("/habit-tracker/delete/99999", follow_redirects=False)

    # Assert
    assert response.status_code == 404


<<<<<<< HEAD
=======


>>>>>>> 35e09164a563985f602da93b4532e4e54108bbd7
def test_habit_tracker_post_saves_predefined_category(logged_in_client, app):
    """Selecting a predefined category stores it on the Habit."""
    form = {
        "name": "Read 10 pages",
        "description": "Night routine",
<<<<<<< HEAD
        "category": "Fitness",  # one of the predefined categories
=======
        "category": "Fitness"
>>>>>>> 35e09164a563985f602da93b4532e4e54108bbd7
    }
    resp = logged_in_client.post("/habit-tracker", data=form, follow_redirects=False)
    assert resp.status_code == 302 and resp.location == "/habit-tracker"

    with app.app_context():
        stored = Habit.query.filter_by(name="Read 10 pages").first()
        assert stored is not None
        assert stored.category == "Fitness"


def test_habit_tracker_post_uses_category_custom_when_other_selected(logged_in_client, app):
    """If category=='other', the value from category_custom is stored."""
    form = {
        "name": "Evening Walk",
        "description": "30 mins",
        "category": "other",
        "category_custom": "Wellness",
    }
    resp = logged_in_client.post("/habit-tracker", data=form, follow_redirects=False)
    assert resp.status_code == 302 and resp.location == "/habit-tracker"

    with app.app_context():
        stored = Habit.query.filter_by(name="Evening Walk").first()
        assert stored is not None
        assert stored.category == "Wellness"


def test_habit_dashboard_displays_category(logged_in_client, app):
    """After creating a habit with a category, the /habit-tracker page shows that category text."""
<<<<<<< HEAD
    # Create a habit with a category
    form = {"name": "Meditation", "description": "Mindful breathing", "category": "Mindfulness"}
=======
    form = {
        "name": "Meditation",
        "description": "Mindful breathing",
        "category": "Mindfulness"
    }
>>>>>>> 35e09164a563985f602da93b4532e4e54108bbd7
    create_resp = logged_in_client.post("/habit-tracker", data=form, follow_redirects=False)
    assert create_resp.status_code == 302

    page_resp = logged_in_client.get("/habit-tracker", follow_redirects=True)
    assert page_resp.status_code == 200
    html = page_resp.data.decode("utf-8")
    assert "Meditation" in html
    assert "Mindfulness" in html



def test_archive_habit_success(logged_in_client, app):
    """Test that POST /habit-tracker/archive/<id> archives a habit successfully."""
    with app.app_context():
        habit = Habit(name='Morning Yoga', description='Daily yoga routine', is_archived=False)
        from extensions import db
        db.session.add(habit)
        db.session.commit()
        habit_id = habit.id
    
    response = logged_in_client.post(f'/habit-tracker/archive/{habit_id}', follow_redirects=False)
    
    assert response.status_code == 302
    assert response.location == '/habit-tracker'
    
    with app.app_context():
        archived_habit = Habit.query.filter_by(id=habit_id).first()
        assert archived_habit is not None
        assert archived_habit.is_archived is True
        assert archived_habit.archived_at is not None


def test_archive_habit_requires_auth(client):
    """Test that archiving a habit without authentication redirects to signin."""
    response = client.post('/habit-tracker/archive/1', follow_redirects=False)
    assert response.status_code == 302
    assert response.location == '/signin'


def test_archive_habit_invalid_id_returns_404(logged_in_client):
    """Test that POST /habit-tracker/archive/<invalid_id> returns 404."""
    response = logged_in_client.post('/habit-tracker/archive/99999', follow_redirects=False)
    assert response.status_code == 404


def test_unarchive_habit_success(logged_in_client, app):
    """Test that POST /habit-tracker/unarchive/<id> unarchives a habit successfully."""
    with app.app_context():
        from datetime import datetime, timezone
        habit = Habit(
            name='Evening Walk',
            description='30 min walk',
            is_archived=True,
            archived_at=datetime.now(timezone.utc)
        )
        from extensions import db
        db.session.add(habit)
        db.session.commit()
        habit_id = habit.id
    
    response = logged_in_client.post(f'/habit-tracker/unarchive/{habit_id}', follow_redirects=False)
    
    assert response.status_code == 302
    
    with app.app_context():
        unarchived_habit = Habit.query.filter_by(id=habit_id).first()
        assert unarchived_habit is not None
        assert unarchived_habit.is_archived is False
        assert unarchived_habit.archived_at is None


def test_unarchive_habit_requires_auth(client):
    """Test that unarchiving a habit without authentication redirects to signin."""
    response = client.post('/habit-tracker/unarchive/1', follow_redirects=False)
    assert response.status_code == 302
    assert response.location == '/signin'


def test_unarchive_habit_invalid_id_returns_404(logged_in_client):
    """Test that POST /habit-tracker/unarchive/<invalid_id> returns 404."""
    response = logged_in_client.post('/habit-tracker/unarchive/99999', follow_redirects=False)
    assert response.status_code == 404


def test_archived_habits_page_get_returns_ok(logged_in_client):
    """Test that GET /habit-tracker/archived returns a 200 status code when authenticated."""
    response = logged_in_client.get('/habit-tracker/archived')
    assert response.status_code == 200


def test_archived_habits_page_requires_auth(client):
    """Test that accessing archived habits page without authentication redirects to signin."""
    response = client.get('/habit-tracker/archived', follow_redirects=False)
    assert response.status_code == 302
    assert response.location == '/signin'


def test_archived_habits_page_shows_only_archived(logged_in_client, app):
    """Test that /habit-tracker/archived page only displays archived habits."""
    with app.app_context():
        from datetime import datetime, timezone
        from extensions import db
        
        active_habit = Habit(name='My Active Habit Item', description='Not archived', is_archived=False)
        archived_habit = Habit(
            name='My Archived Habit Item',
            description='This is archived',
            is_archived=True,
            archived_at=datetime.now(timezone.utc)
        )
        db.session.add(active_habit)
        db.session.add(archived_habit)
        db.session.commit()
    
    response = logged_in_client.get('/habit-tracker/archived')
    html = response.data.decode('utf-8')
    
    assert response.status_code == 200
    assert 'My Archived Habit Item' in html
    assert 'My Active Habit Item' not in html


# === Parametrized Tests ===


@pytest.mark.parametrize("endpoint", ["/habit-tracker"])
def test_all_modules_get_returns_ok(logged_in_client, endpoint):
    """Test that all module endpoints return 200 status code on GET requests when authenticated."""
    response = logged_in_client.get(endpoint)
    assert response.status_code == 200