from flask import Flask, flash, redirect, url_for, abort, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore, signals
from flask_security.forms import LoginForm
from flask_mail import Mail
from flask_migrate import Migrate
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from lotusrpg.config import Config

db = SQLAlchemy()
mail = Mail()

# Initialize limiter
limiter = Limiter(
    key_func=get_remote_address,
    storage_uri="memory://",
    default_limits=["200 per day"]
)

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Initialize extensions
    db.init_app(app)
    mail.init_app(app)
    migrate = Migrate(app, db)
    limiter.init_app(app)

    from lotusrpg.models import User, Role
    from lotusrpg.users.forms import ExtendedRegisterForm
    
    # Setup Flask-Security
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security = Security(
        app, 
        user_datastore,
        register_form=ExtendedRegisterForm,  
        confirm_register_form=ExtendedRegisterForm,  
        render_template_context_processor=lambda: {
            'base_template': 'base.html'
        }
    )

    # Apply rate limit to the security.login view function
    security_login = app.view_functions['security.login']
    app.view_functions['security.login'] = limiter.limit(
        "5 per minute",
        exempt_when=lambda: request.method == "GET"
    )(security_login)

    # Debug route for rate limit status
    @app.route('/debug/ratelimit')
    @limiter.exempt
    def debug_ratelimit():
        if not app.debug:
            abort(404) 
        try:
            ip = get_remote_address()
            return jsonify({
                'remote_addr': ip,
                'limit_info': str(limiter.get_application_limits())
            })
        except Exception as e:
            return jsonify({'error': str(e)})

    # Register blueprints
    from lotusrpg.users.routes import users
    from lotusrpg.main.routes import main
    from lotusrpg.forum.routes import forum
    from lotusrpg.errors.handlers import errors
    from lotusrpg.rules.routes import rules
    from lotusrpg.admin.routes import admin

    app.register_blueprint(users)
    app.register_blueprint(main)
    app.register_blueprint(forum)
    app.register_blueprint(errors)
    app.register_blueprint(rules)
    app.register_blueprint(admin, url_prefix='/admin')

    # Add error handler for rate limit exceeded
    @app.errorhandler(429)
    def ratelimit_handler(e):
        flash("Too many login attempts. Please try the forgot password link below or wait a few minutes.", "danger")
        return render_template(
            'security/login_user.html',
            login_user_form=LoginForm(),
            base_template='base.html'
        ), 429

    return app