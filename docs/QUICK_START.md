# 🚀 Quick Start: Pick Your Module

This guide walks you through selecting one module and removing the rest to create a clean starting point for your project.

## Overview

The Student Starter Pack includes four complete applications. Most students will want to:
1. **Explore** all four modules
2. **Choose** the one that fits their project best
3. **Remove** the others to start with a clean slate

## Step 1: Explore All Modules

First, run the application and test each module:

```bash
uv sync
uv run python app.py
```

Visit `http://localhost:5000` and try out:
- **Habit Tracker** - Track daily habits with streaks
- **Mood Journal** - Log moods with notes
- **Expense Splitter** - Split expenses among participants
- **Recipe Assistant** - Store recipes with ingredients

## Step 2: Choose Your Module

Decide which module best fits your project needs. Below are complete cleanup instructions for each option.

---

## Option 1: Keep Only Habit Tracker

### Remove Other Routes from `app.py`

**Find and delete** these route functions (including all their code):
- `@app.route('/mood-journal', ...)` - Delete the entire mood_journal function
- `@app.route('/expense-splitter', ...)` - Delete the entire expense_splitter function
- `@app.route('/recipe-assistant', ...)` - Delete the entire recipe_assistant function

**Update imports** at the top of `app.py`:

```python
# Change this line:
from models import Habit, MoodEntry, Expense, Recipe

# To this:
from models import Habit
```

### Remove Other Models from `models.py`

Delete these entire class definitions:
- `class MoodEntry(db.Model):` and all its code
- `class Expense(db.Model):` and all its code
- `class Recipe(db.Model):` and all its code

Keep only `class Habit(db.Model):`

### Delete Template Folders

```bash
rm -rf templates/apps/mood_journal
rm -rf templates/apps/expense_splitter
rm -rf templates/apps/recipe_assistant
```

### Update Navigation in `templates/base.html`

Open `templates/base.html` and find the `<nav>` section (around line 26).

**Delete these navigation links:**
- The entire `<a href="/mood-journal">` link (lines 33-38)
- The entire `<a href="/expense-splitter">` link (lines 39-44)
- The entire `<a href="/recipe-assistant">` link (lines 45-50)

Keep only the Habit Tracker link.

### Reset Database

```bash
rm instance/app.db
uv run python -c "from app import app, db; app.app_context().push(); db.create_all()"
```

### Update Home Page (Optional)

Edit `templates/home/index.html` to remove cards for the deleted modules.

---

## Option 2: Keep Only Mood Journal

### Remove Other Routes from `app.py`

**Delete** these route functions:
- `@app.route('/habit-tracker', ...)`
- `@app.route('/expense-splitter', ...)`
- `@app.route('/recipe-assistant', ...)`

**Update imports:**

```python
from models import MoodEntry
```

### Remove Other Models from `models.py`

Delete these classes:
- `class Habit(db.Model):`
- `class Expense(db.Model):`
- `class Recipe(db.Model):`

### Delete Template Folders

```bash
rm -rf templates/apps/habit_tracker
rm -rf templates/apps/expense_splitter
rm -rf templates/apps/recipe_assistant
```

### Update Navigation in `templates/base.html`

Delete the navigation links for Habit Tracker, Expense Splitter, and Recipe Assistant. Keep only Mood Journal.

### Reset Database

```bash
rm instance/app.db
uv run python -c "from app import app, db; app.app_context().push(); db.create_all()"
```

---

## Option 3: Keep Only Expense Splitter

### Remove Other Routes from `app.py`

**Delete** these route functions:
- `@app.route('/habit-tracker', ...)`
- `@app.route('/mood-journal', ...)`
- `@app.route('/recipe-assistant', ...)`

**Update imports:**

```python
from models import Expense
```

### Remove Other Models from `models.py`

Delete these classes:
- `class Habit(db.Model):`
- `class MoodEntry(db.Model):`
- `class Recipe(db.Model):`

### Delete Template Folders

```bash
rm -rf templates/apps/habit_tracker
rm -rf templates/apps/mood_journal
rm -rf templates/apps/recipe_assistant
```

### Update Navigation in `templates/base.html`

Delete the navigation links for Habit Tracker, Mood Journal, and Recipe Assistant. Keep only Expense Splitter.

### Reset Database

```bash
rm instance/app.db
uv run python -c "from app import app, db; app.app_context().push(); db.create_all()"
```

---

## Option 4: Keep Only Recipe Assistant

### Remove Other Routes from `app.py`

**Delete** these route functions:
- `@app.route('/habit-tracker', ...)`
- `@app.route('/mood-journal', ...)`
- `@app.route('/expense-splitter', ...)`

**Update imports:**

```python
from models import Recipe
```

### Remove Other Models from `models.py`

Delete these classes:
- `class Habit(db.Model):`
- `class MoodEntry(db.Model):`
- `class Expense(db.Model):`

### Delete Template Folders

```bash
rm -rf templates/apps/habit_tracker
rm -rf templates/apps/mood_journal
rm -rf templates/apps/expense_splitter
```

### Update Navigation in `templates/base.html`

Delete the navigation links for Habit Tracker, Mood Journal, and Expense Splitter. Keep only Recipe Assistant.

### Reset Database

```bash
rm instance/app.db
uv run python -c "from app import app, db; app.app_context().push(); db.create_all()"
```

---

## Option 5: Keep Multiple Modules

If you want to keep 2-3 modules, just skip the deletion steps for the modules you want to keep. The process is the same:

1. Delete only the routes you don't want
2. Delete only the models you don't want
3. Delete only the templates you don't want
4. Remove only the nav links you don't want
5. Reset the database

---

## Verification Checklist

After cleanup, verify everything works:

- [ ] Run `uv run python app.py` with no errors
- [ ] Visit `http://localhost:5000` - home page loads
- [ ] Navigate to your chosen module - it works correctly
- [ ] Try adding a new item - it saves to database
- [ ] Check that deleted modules don't appear in navigation
- [ ] Restart the app - data persists

## What If I Made a Mistake?

If something breaks:

1. **Check for syntax errors** - Look at the terminal output
2. **Verify imports** - Make sure you didn't delete imported models
3. **Check the database** - Delete and recreate it
4. **Review the code** - Compare with the original files

Or just **restore from git**:

```bash
git checkout app.py models.py templates/base.html
```

Then start over more carefully.

## Next Steps

Now that you have a clean starting point:

1. **Customize your chosen module** - See [CUSTOMIZATION.md](CUSTOMIZATION.md)
2. **Add new features** - Extend the database models and routes
3. **Improve the UI** - Customize Tailwind classes
4. **Add authentication** - See [DEVELOPMENT.md](DEVELOPMENT.md)

## Need Help?

- **Common issues**: See [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
- **Database problems**: See [DATABASE.md](DATABASE.md)
- **Development tips**: See [DEVELOPMENT.md](DEVELOPMENT.md)

---

**Pro Tip:** Before making major changes, commit your clean state to git:

```bash
git add .
git commit -m "Clean project: keeping only [module name]"
```

This creates a checkpoint you can return to if needed.
