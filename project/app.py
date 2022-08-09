import os
from functools import wraps
from pathlib import Path

from flask import (
    Flask,
    render_template,
    request,
    session,
    flash,
    redirect,
    url_for,
    abort,
    jsonify,
)
from flask_sqlalchemy import SQLAlchemy


basedir = Path(__file__).resolve().parent

# configuration
DATABASE = "flaskr.db"
USERNAME = "admin"
PASSWORD = "admin"
SECRET_KEY = "change_me"
url = os.getenv("DATABASE_URL", f"sqlite:///{Path(basedir).joinpath(DATABASE)}")

if url.startswith("postgres://"):
    url = url.replace("postgres://", "postgresql://", 1)

SQLALCHEMY_DATABASE_URI = url
SQLALCHEMY_TRACK_MODIFICATIONS = False


# create and init new flask app
app = Flask(__name__)
# load config
app.config.from_object(__name__)
# init sqlalchemy
db = SQLAlchemy(app)

from project import models


# on home page, prints Hello, World! onto page...
@app.route('/')
def index():
    return "Hello, World!"

if __name__ == "__main__":
   app.run()