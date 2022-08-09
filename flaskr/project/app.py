from flask import Flask

#configuration
DATABASE = "flask.db"

# create and init new flask app
app = Flask(__name__)

# load config
app.config.from_object(__name__)

# on home page, prints Hello, World! onto page...
@app.route("/")
def hello():
  return "Hello, World!"

if __name__ == "__main__":
   app.run()
