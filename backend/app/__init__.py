from Flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy

from config import Config

db = SQLAlchemy()
api = Api()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    api.init_app(app)

    from app import routes

    return app
