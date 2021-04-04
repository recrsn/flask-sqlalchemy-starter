from flask.blueprints import Blueprint

blueprint = Blueprint('index', __name__)


@blueprint.route('/')
def index():
    return "Hello World", 200
