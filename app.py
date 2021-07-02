import os
import requests
from flask import Flask, render_template, Response


app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/chat')
def chat():
    return render_template('chat.html')


if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=False, port=8080, host='0.0.0.0')
