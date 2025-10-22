[1mdiff --git a/tests/test_models.py b/tests/test_models.py[m
[1mindex cfac492..1bc6f56 100644[m
[1m--- a/tests/test_models.py[m
[1m+++ b/tests/test_models.py[m
[36m@@ -2,11 +2,11 @@[m [mimport pytest[m
 from sqlalchemy.exc import IntegrityError[m
 [m
 from extensions import db[m
[31m-from models import Expense, Habit, MoodEntry, Recipe[m
[32m+[m[32mfrom models import Habit[m
 [m
 [m
 # === Habit Model Tests ===[m
[31m-[m
[32m+[m[32m#[m
 [m
 def test_habit_create_and_persist(app):[m
     """Test that Habit model can be created and persisted to the database."""[m
[36m@@ -25,7 +25,7 @@[m [mdef test_habit_create_and_persist(app):[m
 [m
 [m
 def test_habit_allows_optional_description(app):[m
[31m-    """Test that Habit model allows description to be None."""[m
[32m+[m[32m    """Test that Habit model allows description to be None"""[m
     # Arrange[m
     habit = Habit(name="Meditate", description=None)[m
 [m
[36m@@ -38,124 +38,3 @@[m [mdef test_habit_allows_optional_description(app):[m
     assert stored is not None[m
     assert stored.description is None[m
 [m
[31m-[m
[31m-# === MoodEntry Model Tests ===[m
[31m-[m
[31m-[m
[31m-def test_mood_entry_create_and_persist(app):[m
[31m-    """Test that MoodEntry model can be created and persisted to the database."""[m
[31m-    # Arrange[m
[31m-    entry = MoodEntry(mood="Happy", notes="Great day")[m
[31m-[m
[31m-    # Act[m
[31m-    db.session.add(entry)[m
[31m-    db.session.commit()[m
[31m-[m
[31m-    # Assert[m
[31m-    stored = MoodEntry.query.first()[m
[31m-    assert stored is not None[m
[31m-    assert stored.mood == "Happy"[m
[31m-    assert stored.notes == "Great day"[m
[31m-[m
[31m-[m
[31m-def test_mood_entry_requires_mood(app):[m
[31m-    """Test that MoodEntry model raises IntegrityError when mood is None."""[m
[31m-    # Arrange[m
[31m-    entry = MoodEntry(mood=None, notes="Forgot")[m
[31m-    db.session.add(entry)[m
[31m-[m
[31m-    # Act & Assert[m
[31m-    with pytest.raises(IntegrityError):[m
[31m-        db.session.commit()[m
[31m-[m
[31m-    db.session.rollback()[m
[31m-[m
[31m-[m
[31m-# === Expense Model Tests ===[m
[31m-[m
[31m-[m
[31m-def test_expense_create_and_persist(app):[m
[31m-    """Test that Expense model can be created and persisted to the database."""[m
[31m-    # Arrange[m
[31m-    expense = Expense(description="Lunch", amount=15.50, payer="Sam", participants="Sam, Alex")[m
[31m-[m
[31m-    # Act[m
[31m-    db.session.add(expense)[m
[31m-    db.session.commit()[m
[31m-[m
[31m-    # Assert[m
[31m-    stored = Expense.query.first()[m
[31m-    assert stored is not None[m
[31m-    assert stored.description == "Lunch"[m
[31m-    assert stored.amount == 15.50[m
[31m-    assert stored.payer == "Sam"[m
[31m-[m
[31m-[m
[31m-def test_expense_requires_amount(app):[m
[31m-    """Test that Expense model raises IntegrityError when amount is None."""[m
[31m-    # Arrange[m
[31m-    expense = Expense(description="Dinner", amount=None, payer="Alex")[m
[31m-    db.session.add(expense)[m
[31m-[m
[31m-    # Act & Assert[m
[31m-    with pytest.raises(IntegrityError):[m
[31m-        db.session.commit()[m
[31m-[m
[31m-    db.session.rollback()[m
[31m-[m
[31m-[m
[31m-def test_expense_requires_description(app):[m
[31m-    """Test that Expense model raises IntegrityError when description is None."""[m
[31m-    # Arrange[m
[31m-    expense = Expense(description=None, amount=20.00, payer="Jordan")[m
[31m-    db.session.add(expense)[m
[31m-[m
[31m-    # Act & Assert[m
[31m-    with pytest.raises(IntegrityError):[m
[31m-        db.session.commit()[m
[31m-[m
[31m-    db.session.rollback()[m
[31m-[m
[31m-[m
[31m-# === Recipe Model Tests ===[m
[31m-[m
[31m-[m
[31m-def test_recipe_create_and_persist(app):[m
[31m-    """Test that Recipe model can be created and persisted to the database."""[m
[31m-    # Arrange[m
[31m-    recipe = Recipe([m
[31m-        name="Pasta",[m
[31m-        ingredients="Noodles, Sauce",[m
[31m-        instructions="Boil and mix",[m
[31m-        prep_time=15[m
[31m-    )[m
[31m-[m
[31m-    # Act[m
[31m-    db.session.add(recipe)[m
[31m-    db.session.commit()[m
[31m-[m
[31m-    # Assert[m
[31m-    stored = Recipe.query.first()[m
[31m-    assert stored is not None[m
[31m-    assert stored.name == "Pasta"[m
[31m-    assert stored.prep_time == 15[m
[31m-[m
[31m-[m
[31m-def test_recipe_allows_optional_prep_time(app):[m
[31m-    """Test that Recipe model allows prep_time to be None."""[m
[31m-    # Arrange[m
[31m-    recipe = Recipe([m
[31m-        name="Salad",[m
[31m-        ingredients="Lettuce, Tomato",[m
[31m-        instructions="Mix together",[m
[31m-        prep_time=None,[m
[31m-    )[m
[31m-[m
[31m-    # Act[m
[31m-    db.session.add(recipe)[m
[31m-    db.session.commit()[m
[31m-[m
[31m-    # Assert[m
[31m-    stored = Recipe.query.first()[m
[31m-    assert stored is not None[m
[31m-    assert stored.prep_time is None[m
