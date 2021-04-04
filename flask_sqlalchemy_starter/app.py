from flask import Flask

from flask_sqlalchemy_starter import settings
from flask_sqlalchemy_starter.blueprints import index


def create_app():
    app = Flask(__name__)
    settings.init_app(app)

    app.register_blueprint(index.blueprint)

    return app
