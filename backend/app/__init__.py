from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy

from config import Config

db = SQLAlchemy()
main_api = Api()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    main_api.init_app(app)

    from .routes import init_routes
    init_routes(app)  # Add this line for testing
    
    from .api import api as api_namespace
    main_api.add_namespace(api_namespace)

    return app
