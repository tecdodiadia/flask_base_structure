from app import app, socket, r_cli
from flask import render_template, url_for

@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')