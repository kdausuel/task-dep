import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') 
    if not SECRET_KEY:
        raise ValueError("No SECRET_KEY set for Flask app.")
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    if not SQLALCHEMY_DATABASE_URI:
        raise ValueError("No DATABASE_URL set.")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Security settings
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SECURE = os.environ.get('SESSION_COOKIE_SECURE', 'True').lower() == 'true'

    # Logging
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT', 'False').lower() == 'true'

    # Performance
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_size': int(os.environ.get('POOL_SIZE', 10)),
        'pool_recycle': int(os.environ.get('POOL_RECYCLE', 3600)),
    }

    DEBUG = os.environ.get('FLASK_ENV') == 'development'