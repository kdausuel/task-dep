from flask import request
from flask_restx import Resource, fields
from app import db
from app.models import Task

# Add this function to initialize routes
def init_routes(app):
    @app.route('/')
    def hello_world():
        try:
            db.create_all()
            new_task = Task(title="Test Task", description="This is a test task")
            db.session.add(new_task)
            db.session.commit()
            return f'Hello, Docker! Database is connected. Created task with id: {new_task.id}'
        except Exception as e:
            return f'Hello, Docker! Error connecting to database: {str(e)}'