from flask import render_template
from flask.blueprints import Blueprint

blueprint = Blueprint('index', __name__)


@blueprint.route('/')
def index():
    return render_template('index.html')
