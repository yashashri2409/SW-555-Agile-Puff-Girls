from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev-secret-key-change-in-production'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/')
def home():
    return render_template('home/index.html', page_id='home')

@app.route('/habit-tracker')
def habit_tracker():
    return render_template('apps/habit_tracker/index.html', page_id='habit-tracker')

@app.route('/mood-journal')
def mood_journal():
    return render_template('apps/mood_journal/index.html', page_id='mood-journal')

@app.route('/expense-splitter')
def expense_splitter():
    return render_template('apps/expense_splitter/index.html', page_id='expense-splitter')

@app.route('/recipe-assistant')
def recipe_assistant():
    return render_template('apps/recipe_assistant/index.html', page_id='recipe-assistant')

def init_db():
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    if not os.path.exists('app.db'):
        init_db()
    app.run(debug=True)
