from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
@app.route("/")
def hello_godbay():
    return "<p>Hello, godbay!</p>"

