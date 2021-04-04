from flask import Flask

from . import db
from . import settings
from .blueprints import index, messages


def create_app():
    app = Flask(__name__)
    settings.init_app(app)
    db.init_app(app)

    app.register_blueprint(index.blueprint)
    app.register_blueprint(messages.blueprint, url_prefix='/messages')

    return app
