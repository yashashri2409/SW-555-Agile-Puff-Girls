# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository is a "Student Starter Pack" for SSW555 students. It ships four independent starter applications you can keep or remove individually:
- **Habit Tracker**
- **Mood Journal**
- **Expense Splitter**
- **Recipe Assistant**

Each module lives in its own template folder (`templates/apps/<app-name>`), shares a common layout, and can be deleted without breaking the others. The pack uses Flask + SQLAlchemy on SQLite and demonstrates basic form handling and database writes for each app.

## Development Commands

### Environment Setup
```bash
# Install dependencies
uv sync

# Activate virtual environment
source .venv/bin/activate  # On Unix/macOS
# or
.venv\Scripts\activate  # On Windows
```

### Run Development Server
```bash
uv run python app.py
# or with activated venv:
python app.py
```

### Database Operations
```bash
# Initialize database (happens automatically on first run)
uv run python -c "from app import app, db; app.app_context().push(); db.create_all()"

# Reset database
rm app.db
uv run python -c "from app import app, db; app.app_context().push(); db.create_all()"
```

### Add New Dependencies
```bash
uv add <package-name>
```

## Architecture

### Core Structure
- `app.py`: Main Flask application with route definitions, form handlers, and model imports
- `extensions.py`: Exposes the shared SQLAlchemy instance (`db = SQLAlchemy()`); imported into both `app.py` and `models.py`
- `models.py`: SQLAlchemy database models for all four apps
- `templates/`: Jinja2 templates
  - `base.html`: Shared layout, navigation, and starter-pack branding
  - `home/index.html`: Explains how to pick a module and remove the rest
  - `apps/<app-name>/index.html`: Individual module templates, each rendering form data passed from the route
- `static/css/style.css`: Global styling plus per-module theme variables

### Database Models
Each app has its own model in `models.py`:
- `Habit`: Stores habit name, description, creation date, and completion dates
- `MoodEntry`: Records mood selections and notes with timestamps
- `Expense`: Tracks shared expenses with payer and participants
- `Recipe`: Stores recipe details including ingredients and instructions

### Request Flow
- Routes accept both `GET` and `POST`. On `POST`, form data is validated, persisted with `db.session`, and the user is redirected back to the same route (POST-redirect-GET) so the list refreshes.
- Each template expects its data context (`habits`, `entries`, `expenses`, `recipes`) and renders a styled list with placeholder copy when empty.

### Key Design Principles
1. **Simplicity First**: Each app demonstrates minimal patterns you can extend
2. **Independent Modules**: Deleting a module is safe—remove its template folder, route, and related model
3. **Shared Styling**: Base layout + themed CSS variables keep modules visually distinct but cohesive
4. **No Authentication**: Currently single-user/sample data only

## Expansion Considerations

When adding features:
- Keep individual app logic separate (consider blueprints as modules grow)
- Use Flask blueprints if apps grow complex
- Consider adding user authentication before multi-user features
- Database migrations will be needed when modifying models (consider adding Flask-Migrate)
- Form validation and CSRF protection should be added for production use
- If you remove a module, delete its model and table or run a migration to keep the schema tidy
