# 🚀 Student Starter Pack - SSW555 Project Template

A collection of beautifully designed, production-ready web applications built with Flask, SQLAlchemy, and Tailwind CSS. Perfect for students looking to jumpstart their SSW555 course projects.

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0+-green.svg)
![Tailwind](https://img.shields.io/badge/Tailwind_CSS-3.0-38B2AC.svg)
![License](https://img.shields.io/badge/license-MIT-brightgreen.svg)

## ✨ Features

### 🎯 Four Complete Applications

#### 🌱 **Habit Tracker**
Build better habits with a minimalist, zen-inspired interface
- Daily habit tracking with streak counters
- Progress visualization
- Mindful design philosophy
- Perfect for: Personal development apps, wellness platforms

#### ☁️ **Mood Journal**
Track emotional wellness with beautiful visualizations
- 5-point mood scale with emojis
- Daily reflection notes
- Mood pattern tracking
- Perfect for: Mental health apps, journaling platforms

#### 💳 **Expense Splitter**
Modern finance tracker with terminal-inspired aesthetics
- Smart expense splitting calculations
- Multi-participant support
- Transaction history
- Perfect for: Fintech apps, group expense management

#### 🍳 **Recipe Assistant**
Organize your culinary adventures with a warm, inviting design
- Recipe storage with ingredients and instructions
- Prep time tracking
- Beautiful recipe cards
- Perfect for: Food apps, meal planning platforms

## 🛠️ Tech Stack

- **Backend:** Flask 3.0+ (Python web framework)
- **Database:** SQLAlchemy with SQLite
- **Frontend:** Tailwind CSS (via CDN)
- **UI Components:** Modern, responsive design
- **Architecture:** Modular, MVC pattern

## 🚀 Quick Start

### Prerequisites

- Python 3.9 or higher
- uv (Python package manager) - [Install uv](https://github.com/astral-sh/uv)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/SSW555-Example-Project.git
cd SSW555-Example-Project
```

2. **Install dependencies using uv**
```bash
uv sync
```

3. **Activate the virtual environment**
```bash
source .venv/bin/activate  # On Unix/macOS
# or
.venv\Scripts\activate  # On Windows
```

4. **Run the application**
```bash
python app.py
```

5. **Open your browser**
Navigate to `http://localhost:5000`

## 📁 Project Structure

```
SSW555-Example-Project/
│
├── app.py                 # Main Flask application
├── models.py             # Database models
├── extensions.py         # Shared extensions (SQLAlchemy)
├── requirements.txt      # Python dependencies
│
├── templates/            # HTML templates
│   ├── base.html        # Base layout with navigation
│   ├── home/            # Home page
│   └── apps/            # Individual applications
│       ├── habit_tracker/
│       ├── mood_journal/
│       ├── expense_splitter/
│       └── recipe_assistant/
│
├── static/              # Static files
│   └── css/
│       └── style.css    # Global styles
│
└── app.db              # SQLite database (auto-created)
```

## 🎨 Customization Guide

### Choosing Your Module

1. **Explore all modules** at `http://localhost:5000`
2. **Pick the one** that best fits your project needs
3. **Remove unwanted modules:**

```python
# In app.py, remove unwanted routes
# For example, to keep only Habit Tracker:

# Remove these imports
# from models import MoodEntry, Expense, Recipe

# Remove these routes
# @app.route('/mood-journal', ...)
# @app.route('/expense-splitter', ...)
# @app.route('/recipe-assistant', ...)
```

4. **Delete template folders** you don't need from `templates/apps/`

### Adding New Features

Each module is designed to be easily extensible:

```python
# Example: Adding a new field to Habit model
class Habit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    category = db.Column(db.String(50))  # New field
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
```

### Styling Customization

The project uses Tailwind CSS via CDN. You can customize the design by:

1. **Modifying color schemes** in the templates
2. **Adding custom CSS** in the `<style>` blocks
3. **Using Tailwind utility classes** directly in HTML

## 🔧 Database Operations

### Initialize/Reset Database

```bash
# Delete existing database
rm app.db

# Create new database
python -c "from app import app, db; app.app_context().push(); db.create_all()"
```

### Database Migrations (Advanced)

For production use, consider adding Flask-Migrate:

```bash
uv add flask-migrate
```

## 🧪 Development Tips

### Running in Debug Mode
The app runs in debug mode by default for development:
```python
app.run(debug=True)
```

### Adding Authentication
Consider adding Flask-Login for user authentication:
```bash
uv add flask-login
```

### Environment Variables
Create a `.env` file for configuration:
```env
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///app.db
```

## 📚 Learning Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [SQLAlchemy Tutorial](https://docs.sqlalchemy.org/en/20/tutorial/)
- [Tailwind CSS Docs](https://tailwindcss.com/docs)
- [Python Best Practices](https://docs.python-guide.org/)

## 🤝 Contributing

This is a student project template. Feel free to:
- Fork and customize for your needs
- Submit issues for bugs
- Share your modifications with classmates

## 📝 License

This project is open source and available under the MIT License.

## 🎓 Course Information

**Course:** SSW555 - Agile Methods for Software Development
**Institution:** Stevens Institute of Technology
**Purpose:** Educational project template for rapid prototyping

## 💡 Tips

1. **Start Simple:** Pick one module and master it before adding complexity
2. **Version Control:** Commit your changes frequently
3. **Documentation:** Update this README as you customize
4. **Testing:** Add unit tests as you build features
5. **Deployment:** Consider using Heroku, Railway, or PythonAnywhere for free hosting

## 🚨 Common Issues & Solutions

### Issue: `uv: command not found`
**Solution:** Install uv first:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Issue: Port 5000 already in use
**Solution:** Change the port in app.py:
```python
app.run(debug=True, port=5001)
```

### Issue: Database locked error
**Solution:** Ensure only one instance of the app is running

## 🌟 Showcase Your Work

Built something cool with this template? Let us know!
- Add a star ⭐ to this repository
- Share your project in class
- Contribute improvements back to the template

---

**Happy Coding!** 🎉

*Built with ❤️ for SSW555 students*