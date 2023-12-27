from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<center><h1>Hello, Azure Web Apps!</h1></center>"
