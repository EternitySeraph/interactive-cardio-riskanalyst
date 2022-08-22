import os
from pathlib import Path

from flask import (
    Flask,
)
from flask_sqlalchemy import SQLAlchemy

from src import create_main_dash

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


# on home page, uses base as template
@app.route('/')
def index():
    return create_main_dash(app)


if __name__ == "__main__":
    app.run()
