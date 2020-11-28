from flask import Flask

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
    pass