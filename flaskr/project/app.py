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


# on home page, prints database entries onto page...
@app.route('/')
def index():
    """Searches the database for entries, then displays them."""
    entries = db.session.query(models.Post)
    return render_template('index.html', entries=entries)

if __name__ == "__main__":
   app.run()
