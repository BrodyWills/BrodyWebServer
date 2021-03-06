import os
from flask import Flask, render_template

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
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
