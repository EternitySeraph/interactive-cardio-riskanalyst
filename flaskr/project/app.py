from flask import Flask

# create and init new flask app
app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello, World!"

if __name__ == "__main__":
   app.run()
