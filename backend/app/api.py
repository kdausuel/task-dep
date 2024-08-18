from flask_restx import Namespace, Resource, fields
from app import db
from app.models import Task, Dependency

api = Namespace('api', description='Task Dependency Visualizer API')

task_model = api.model('Task', {
    'id': fields.Integer(readonly=True, description='The task unique identifier'),
    'title': fields.String(required=True, description='The task title'),
    'description': fields.String(description='The task description'),
    'status': fields.String(description='The task status'),
    'created_at': fields.DateTime(readonly=True, description='The creation date of the task'),
    'updated_at': fields.DateTime(readonly=True, description='The last update date for the task')
    })

@api.route('/test')
class TestAPI(Resource):
    def get(self):
        """Test if the API is working"""
        return {'message': 'API is working!'}, 200

    
@api.route('/tasks')
class TaskList(Resource):
    @api.doc('list_tasks')
    @api.marshal_list_with(task_model)
    def get(self):
        """List all tasks"""
        return Task.query.all()
    
    @api.doc('create_task')
    @api.expect(task_model)
    @api.marshal_with(task_model, code=201)
    def post(self):
        """Create a new task"""
        data = api.payload
        new_task = Task(
            title = data['title'],
            description = data.get('description', ''),
            status = data.get('status', 'Not Started')
            )
        db.session.add(new_task)
        db.session.commit()
        return new_task, 201

@api.route('/tasks/<int:id>')
@api.param('id', 'The task identifier')
@api.response(404, 'Task not found')
class TaskItem(Resource):
    @api.doc('get_task')
    @api.marshal_with(task_model)
    def get(self, id):
        """Fetch a task given its id"""
        task = Task.query.get_or_404(id)
        return task
    
    @api.doc('update_task')
    @api.expect(task_model)
    @api.marshal_with(task_model)
    def put(self, id):
        """Update a task given its id"""
        task = Task.query_or_404(id)
        data = api.payload
        task.title = data['title']
        task.description = data.get('description', task.description)
        task.status = data.get('status', task.status)
        db.session.commit()
        return task
    
    @api.doc('delete_task')
    @api.response(204, 'Task deleted')
    def delete(self, id):
        """Delete a task given its id"""
        task = Task.query_or_404(id)
        db.session.delete(task)
        db.session.commit()
        return '', 204
    
