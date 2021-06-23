"""Core Application Module"""
from config import config_factory
from flask import Flask
from routes import api_bp


def create_app(stage: str) -> Flask:
    app = Flask(__name__)
    config = stage if stage in config_factory else 'development'
    app.config.from_object(config_factory[config])

    app.register_blueprint(api_bp)
    return app
