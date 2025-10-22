from extensions import db
from datetime import datetime

class Habit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    category = db.Column(db.String(60))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    completed_dates = db.Column(db.Text)
