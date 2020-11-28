from flask import Flask
from flask import render_template
import requests

app = Flask(__name__)


@app.route('/hello')
def hello_world():
    """
    $ export FLASK_APP=hello.py
    $ flask run
    """
    return 'Hello world'


@app.route('/')
def posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    return render_template('index.html', posts=response.json())
