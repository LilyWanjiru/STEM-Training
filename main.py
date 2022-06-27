from cProfile import run
from flask import Flask
from pip import main

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello world"