import flask
from flask import Flask, render_template

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/workplan/<id>')
def workplan(id):
    return flask.render_template('workplan.html', id=id)