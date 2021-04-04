import os

import flask_migrate
import pytest

from flask_sqlalchemy_starter.app import create_app


@pytest.fixture(scope="session", autouse=True)
def app():
    # To use databases like Postgres, you can use testcontainers
    # https://github.com/testcontainers/testcontainers-python
    # with PostgresContainer('postgres:13') as postgres:
    #     os.environ['DATABASE_URI'] = postgres.get_connection_url()

    if os.path.exists('../test.sqlite3'):
        os.remove('../test.sqlite3')

    os.environ['DATABASE_URI'] = 'sqlite:///../test.sqlite3'

    flask_app = create_app()
    flask_app.config['TESTING'] = True

    with flask_app.app_context():
        flask_migrate.upgrade()

    yield flask_app
