from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore
from flask_mail import Mail
from flask_migrate import Migrate
from lotusrpg.config import Config 


db = SQLAlchemy()
mail = Mail()

def create_app(config_class=Config):
    
    app = Flask(__name__)
    app.config.from_object(Config)
    security = Security(app)
    db.init_app(app)
    mail.init_app(app)

    migrate = Migrate(app, db)

    from lotusrpg.models import User, Role
    from lotusrpg.users.forms import ExtendedRegisterForm
    
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security = Security(
        app, 
        user_datastore,
        register_form=ExtendedRegisterForm,  # Pass the class directly
        confirm_register_form=ExtendedRegisterForm,  # Add this line too
        render_template_context_processor=lambda: {
            'base_template': 'base.html'
        }
    )

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

    return app