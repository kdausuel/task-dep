from app import db
from datetime import datetime, timezone

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    status = db.Column(db.String(20), default='Not Started')
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))

    # Relations
    dependencies = db.relationship('Dependency', foreign_keys='Dependency.dependent_id', backref='dependent', lazy='dynamic')
    dependents = db.relationship('Dependency', foreign_keys='Dependency.dependency_id', backref='dependency', lazy='dynamic')

    def __repr__(self):
        return f'<Task {self.id}>'
    
class Dependency(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dependent_id = db.Column(db.Integer, db.ForeignKey('task.id'), nullable=False)
    dependency_id = db.Column(db.Integer, db.ForeignKey('task.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))

    def __repr__(self):
        return f'<Dependency {self.id}: {self.dependency_id} -> {self.dependency_id}>'
    