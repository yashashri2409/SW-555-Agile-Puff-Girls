# SSW555-Example-Project

Multi-App Platform - A Flask-based demonstration project for SSW 555 - Agile Methods for Software Development.

## Features

This project provides a foundation for four expandable applications:

- **Habit Tracker** - Build and track daily habits
- **Mood Journal** - Record and reflect on daily emotions
- **Expense Splitter** - Manage shared expenses with others
- **Recipe Assistant** - Store and organize your favorite recipes

## Quick Start

1. **Install dependencies:**
   ```bash
   uv sync
   ```

2. **Run the application:**
   ```bash
   uv run python app.py
   ```

3. **Access the application:**
   Open your browser and navigate to `http://localhost:5000`

## Technology Stack

- **Backend:** Flask (Python web framework)
- **Database:** SQLite with SQLAlchemy ORM
- **Frontend:** HTML templates with Jinja2
- **Package Manager:** uv (fast Python package installer)
- **Styling:** Custom CSS

## Project Structure

```
├── app.py              # Main Flask application
├── models.py           # Database models
├── templates/          # HTML templates
│   ├── base.html      # Base template with navigation
│   ├── home.html      # Landing page
│   └── ...            # Individual app templates
├── static/            # Static assets
│   └── css/
│       └── style.css  # Styling
└── app.db             # SQLite database (auto-created)
```

## Development

This project is designed to be simple and expandable. Each application module is independent and can be enhanced with additional features as needed.

For development guidance, see [CLAUDE.md](CLAUDE.md).

## License

MIT License - see [LICENSE](LICENSE) file for details.
