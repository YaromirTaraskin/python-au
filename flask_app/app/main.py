import operator
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route("/another-page/")
def another_page():
    return "Еще одна страница"


@app.route('/albums/1')
def hello_world():
    return 'Hello, Flask'


@app.route('/albums/<album_number>')
def albums(album_number):
    return f'The {album_number} album.'


@app.route('/albums/<int:album_number>/<song_number>')
def albums(album_number, song_number):
    return f'The {album_number} album and {song_number} musician performer.'


@app.route('/contact/')
def contact():
    return 'contact information'


@app.route('/calculate/<int:a>/<int:b>/')
def calculate(a, b):
    return str(a**b)


@app.route("/<int:num>/")
def next_num(num):
    return str(num + 1)


operations = dict(zip(('+', ':', '**', '-', '*'),
                      (operator.add, operator.truediv, operator.pow, operator.sub, operator.mul)))


@app.route('/<int:a><string:op><int:b>/')
def route_calculator(a, op, b):
    return str(operations[op](a, b))


if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)
