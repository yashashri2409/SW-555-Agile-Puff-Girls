# 🚀 Student Starter Pack - SSW555 Project Template

A collection of beautifully designed, production-ready web applications built with Flask, SQLAlchemy, and Tailwind CSS. Perfect for students looking to jumpstart their SSW555 course projects.

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0+-green.svg)
![Tailwind](https://img.shields.io/badge/Tailwind_CSS-3.0-38B2AC.svg)
![License](https://img.shields.io/badge/license-MIT-brightgreen.svg)

## ✨ What's Inside

Four complete, production-ready applications to choose from:

- **🌱 Habit Tracker** - Daily habit tracking with streak counters and progress visualization
- **☁️ Mood Journal** - Emotional wellness tracking with mood scales and reflection notes
- **💳 Expense Splitter** - Smart expense splitting with multi-participant support
- **🍳 Recipe Assistant** - Recipe storage with ingredients, instructions, and prep time tracking

Each app features modern UI design, form handling, and database persistence. Pick one, customize it, and build your project on top of it!

**➡️ New to the starter pack? Start here: [Quick Start Guide](docs/QUICK_START.md)**

## ⚡ Installation

### Prerequisites

- Python 3.9+
- [uv](https://github.com/astral-sh/uv) (Python package manager)

### Installation

```bash
# Clone and navigate
git clone https://github.com/yourusername/SSW555-Example-Project.git
cd SSW555-Example-Project

# Install dependencies
uv sync

# Run the application (uv automatically handles the virtual environment)
uv run python app.py

# Open browser at http://localhost:5000
```

## 📁 Project Structure

```
SSW555-Example-Project/
├── app.py              # Main Flask application with routes
├── models.py           # Database models (Habit, MoodEntry, Expense, Recipe)
├── extensions.py       # Shared SQLAlchemy instance
├── pyproject.toml      # Project dependencies (managed by uv)
├── uv.lock             # Dependency lock file
│
├── docs/               # Documentation
│   ├── CUSTOMIZATION.md
│   ├── DATABASE.md
│   ├── DEVELOPMENT.md
│   └── TROUBLESHOOTING.md
│
├── templates/          # Jinja2 templates
│   ├── base.html       # Shared layout & navigation
│   ├── home/           # Landing page
│   └── apps/           # Individual app templates
│       ├── habit_tracker/
│       ├── mood_journal/
│       ├── expense_splitter/
│       └── recipe_assistant/
│
├── static/             # Static files
│   └── css/
│       └── style.css   # Global styles
│
└── instance/           # Instance-specific files (auto-created)
    └── app.db          # SQLite database
```

## 🎨 Customization

### Choosing Your Module

1. Explore all modules at `http://localhost:5000`
2. Pick the one that fits your project
3. Remove unwanted routes from `app.py`
4. Delete unused template folders from `templates/apps/`

**📖 Detailed guide:** [docs/CUSTOMIZATION.md](docs/CUSTOMIZATION.md)

### Next Steps

- **Extend models** - Add new fields or relationships
- **Create new routes** - Build additional features
- **Customize styling** - Modify Tailwind classes or add custom CSS
- **Add authentication** - Use Flask-Login for user management

## 📚 Documentation

- **[Quick Start Guide](docs/QUICK_START.md)** ⭐ - Pick a module and clean up the rest (start here!)
- **[Customization Guide](docs/CUSTOMIZATION.md)** - How to choose modules, add features, and customize styling
- **[Database Management](docs/DATABASE.md)** - Schema operations, migrations, and query examples
- **[Development Guide](docs/DEVELOPMENT.md)** - Advanced features, testing, API development, deployment
- **[Troubleshooting](docs/TROUBLESHOOTING.md)** - Common issues and solutions

## 🛠️ Tech Stack

- **Backend:** Flask 3.0+ with SQLAlchemy
- **Database:** SQLite (easy to switch to PostgreSQL)
- **Frontend:** Tailwind CSS (via CDN)
- **Architecture:** Modular MVC pattern

## 🎓 Course Information

**Course:** SSW555 - Agile Methods for Software Development
**Institution:** Stevens Institute of Technology
**Purpose:** Educational template for rapid prototyping

## 🤝 Contributing

This is a student project template. Feel free to:
- Fork and customize for your needs
- Submit issues for bugs
- Share improvements with classmates

## 📝 License

MIT License - Open source and free to use

---

**Happy Coding!** 🎉

*Built with ❤️ for SSW555 students*