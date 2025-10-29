from datetime import datetime

from extensions import db


class ThemePreference(db.Model):
    """Model for storing user theme preferences."""

    id = db.Column(db.Integer, primary_key=True)
    preference = db.Column(db.String(10), default="light")  # 'light' or 'dark'
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Habit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    category = db.Column(db.String(60))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    completed_dates = db.Column(db.Text)
