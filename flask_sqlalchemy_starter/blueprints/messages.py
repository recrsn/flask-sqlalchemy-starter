import secrets

from flask import abort, render_template, redirect, url_for, request
from flask.blueprints import Blueprint

from .. import db
from ..models.message import Message

blueprint = Blueprint('messages', __name__)


@blueprint.route('/<_id>')
def get(_id):
    message = Message.get(_id)

    if not message:
        abort(404)

    return render_template('message.html', message=message), 200


@blueprint.route('/', methods=['POST'])
def create():
    title = request.form.get('title')
    content = request.form.get('content')
    message_id = secrets.token_urlsafe(32)

    message = Message(id=message_id, title=title, content=content)

    with db.transaction():
        db.persist(message)

    return redirect(url_for('messages.get', _id=message_id))


@blueprint.route('/<_id>/delete', methods=['POST'])
def delete(_id):
    message = Message.get(_id)

    if not message:
        abort(404)

    with db.transaction():
        db.delete(message)

    return redirect(url_for('index.index'))
