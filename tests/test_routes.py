import pytest

from app import otp_store
from models import Habit

# === Habit Tracker Tests ===

# === Sign-in and Auth Tests (User Story 01 - NEW SECTION) ===


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


def test_logout_clears_session(
    client,
):  # GREEN COMMENT: CHANGED TO USE 'client' instead of 'logged_in_client' to get a clean session.
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


# === Sign-in and Auth Tests end here ===


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


# === Parametrized Tests ===


@pytest.mark.parametrize("endpoint", ["/habit-tracker"])
def test_all_modules_get_returns_ok(logged_in_client, endpoint):
    """Test that all module endpoints return 200 status code on GET requests when authenticated."""
    # Act
    response = logged_in_client.get(endpoint)

    # Assert
    assert response.status_code == 200
