import sqlite3
from pathlib import Path

from flask import Flask, g, render_template, request, session, flash, redirect, url_for, abort, js


basedir = Path(__file__).resolve().parent

# configuration
DATABASE = "flaskr.db"
USERNAME = "admin"
PASSWORD = "admin"
SECRET_KEY = "change_me"
SQLALCHEMY_DATABASE_URI = f'sqlite:///{Path(basedir).
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
