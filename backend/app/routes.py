from flask import request
from flask_restx import Resource, fields
from app import api, db
from app.models import Task

task_model = api.model('Task', {
    'id': fields.Integer(readonly=True),
    'title': fields.String(required=True),
    'description': fields.String(),
    'completed': fields.Boolean()
    })

@api.route('/tasks')
class TaskList(Resource):
    @api.marshal_list_with(task_model)
    def get(self):
        return Task.query.all()
    
    