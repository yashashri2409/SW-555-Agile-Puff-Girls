from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import os
import random

from extensions import db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev-secret-key-change-in-production'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

from models import Habit

# Store OTPs temporarily
otp_store = {}

@app.route('/')
def home():
    """Landing page"""
    return render_template('home/index.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    """Sign in with OTP"""
    if request.method == 'POST':
        data = request.get_json()
        
        if 'email' in data and 'action' not in data:
            # Generate OTP
            email = data['email']
            otp = str(random.randint(100000, 999999))
            otp_store[email] = otp
            
            print(f"\n{'='*50}")
            print(f"OTP for {email}: {otp}")
            print(f"{'='*50}\n")
            
            return jsonify({'success': True, 'message': f'OTP sent to {email}', 'otp': otp})
        
        elif 'action' in data and data['action'] == 'verify':
            # Verify OTP
            email = data['email']
            otp = data['otp']
            
            if email in otp_store and otp_store[email] == otp:
                session['authenticated'] = True
                session['email'] = email
                del otp_store[email]
                return jsonify({'success': True, 'message': 'Authentication successful'})
            else:
                return jsonify({'success': False, 'message': 'Invalid OTP'})
    
    return render_template('home/signIn.html')

@app.route('/habit-tracker', methods=['GET', 'POST'])
def habit_tracker():
    """Habit tracker - protected"""
    if not session.get('authenticated'):
        return redirect(url_for('signin'))
    
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        description = request.form.get('description', '').strip()

        if name:
            habit = Habit(name=name, description=description or None)
            db.session.add(habit)
            db.session.commit()

        return redirect(url_for('habit_tracker'))

    habits = Habit.query.order_by(Habit.created_at.desc()).all()
    return render_template('apps/habit_tracker/index.html', page_id='habit-tracker', habits=habits)

@app.route('/habit-tracker/delete/<int:habit_id>', methods=['POST'])
def delete_habit(habit_id):
    habit = Habit.query.get_or_404(habit_id)
    db.session.delete(habit)
    db.session.commit()
    return redirect(url_for('habit_tracker'))

# test change
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))
@app.route('/habit-tracker/complete/<int:habit_id>', methods=['POST'])
def complete_habit(habit_id):
    """Mark a habit as complete"""
    habit = Habit.query.get_or_404(habit_id)
    habit.completed = True
    db.session.commit()
    return redirect(url_for('habit_tracker'))


def init_db():
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    if not os.path.exists('app.db'):
        init_db()
    app.run(debug=True,port=8080)