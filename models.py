from extensions import db
from datetime import datetime

class Habit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    completed_dates = db.Column(db.Text)
    is_archived = db.Column(db.Boolean, default=False)  # ADD THIS LINE
    archived_at = db.Column(db.DateTime, nullable=True)  # ADD THIS LINE

