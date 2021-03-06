import os

from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

load_dotenv("dev.env")

db = SQLAlchemy()
migrate = Migrate()

from api import index, order


def create_app(config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)

    app.config.from_object(os.environ.get("APP_SETTINGS"))

    db.init_app(app)
    migrate.init_app(app, db)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # add models to apply changes
    from models import pizza
    from models import order as order_model

    # Register blueprints
    app.register_blueprint(index.bp, url_prefix="/api")
    app.register_blueprint(order.bp, url_prefix="/api")

    return app
