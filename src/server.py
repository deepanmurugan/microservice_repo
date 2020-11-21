from flask import Flask
app = Flask(__name__)

@app.route("/service2")
def hello():
    return "Hello World from service-2"
