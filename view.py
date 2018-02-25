from app import app
from flask import render_template

@app.route('/')
def index():
    name = 'Вова'
    return render_template('index1.html', n = name)