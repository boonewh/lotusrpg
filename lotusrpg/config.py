import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default-secret-key')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')  # Render provides this
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disables overhead for tracking modifications in SQLAlchemy

    # Ensure SSL is used for Render's PostgreSQL
    SQLALCHEMY_ENGINE_OPTIONS = {
        "pool_pre_ping": True,  # Helps with database connection reliability
        "connect_args": {"sslmode": "require"}  # Enforces SSL for database connection
    }

    # reCAPTCHA configuration
    RECAPTCHA_PUBLIC_KEY = os.environ.get('RECAPTCHA_PUBLIC_KEY', '')
    RECAPTCHA_PRIVATE_KEY = os.environ.get('RECAPTCHA_PRIVATE_KEY', '')
    RECAPTCHA_USE_SSL = False
    RECAPTCHA_OPTIONS = {'theme': 'light'}

    # Email configuration
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'mail.gandi.net')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', 465))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'false').lower() in ['true', '1', 't']
    MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL', 'true').lower() in ['true', '1', 't']
    MAIL_USERNAME = os.environ.get('EMAIL_ADDRESS', '')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD', '')

    # Flask-Security settings
    SECURITY_PASSWORD_SALT = os.environ.get('SECURITY_PASSWORD_SALT', 'default-salt')
    SECURITY_PASSWORD_HASH = 'bcrypt'
    SECURITY_REGISTERABLE = True
    SECURITY_RECOVERABLE = True
    SECURITY_TRACKABLE = True
    SECURITY_CONFIRMABLE = True
    SECURITY_USER_IDENTITY_ATTRIBUTES = [
        {'email': {'mapper': lambda x: x, 'case_insensitive': True}},
        {'username': {'mapper': lambda x: x, 'case_insensitive': True}}
    ]
    
    # URL settings for Flask-Security
    SECURITY_LOGIN_URL = '/login'
    SECURITY_LOGOUT_URL = '/logout'
    SECURITY_REGISTER_URL = '/register'
    SECURITY_RESET_URL = '/reset'
    SECURITY_CHANGE_URL = '/change'
    
    # Template paths (using custom templates)
    SECURITY_BLUEPRINT_NAME = 'security'
    SECURITY_URL_PREFIX = None
    SECURITY_TEMPLATE_DIR = 'security'

    # Redirect after login/logout
    SECURITY_POST_LOGIN_VIEW = '/'
    SECURITY_POST_LOGOUT_VIEW = '/'
