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
    return render_template('home.html')

@app.route('/habit-tracker')
def habit_tracker():
    return render_template('habit_tracker.html')

@app.route('/mood-journal')
def mood_journal():
    return render_template('mood_journal.html')

@app.route('/expense-splitter')
def expense_splitter():
    return render_template('expense_splitter.html')

@app.route('/recipe-assistant')
def recipe_assistant():
    return render_template('recipe_assistant.html')

def init_db():
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    if not os.path.exists('app.db'):
        init_db()
    app.run(debug=True)