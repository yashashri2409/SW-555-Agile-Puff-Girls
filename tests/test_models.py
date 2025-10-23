import pytest
from sqlalchemy.exc import IntegrityError

from extensions import db
from models import Habit


# === Habit Model Tests ===
#

def test_habit_create_and_persist(app):
    """Test that Habit model can be created and persisted to the database."""
    # Arrange
    habit = Habit(
        name="Exercise",
        description="Morning routine",
        category="Fitness",
        completed_dates=""
    )

    # Act
    db.session.add(habit)
    db.session.commit()

    # Assert
    stored = Habit.query.first()
    assert stored is not None
    assert stored.name == "Exercise"
    assert stored.description == "Morning routine"
    assert stored.category == "Fitness"
    assert stored.completed_dates == ""


def test_habit_allows_optional_fields(app):
    """Test that Habit model allows nullable fields like description and category."""
    # Arrange
    habit = Habit(name="Meditate", description=None, category=None)

    # Act
    db.session.add(habit)
    db.session.commit()

    # Assert
    stored = Habit.query.first()
    assert stored is not None
    assert stored.description is None
    assert stored.category is None

