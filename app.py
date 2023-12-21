import flask
from flask import Flask, render_template

app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/workplan/<id>')
def workplan(id):
    return flask.render_template('workplan.html', id=id)