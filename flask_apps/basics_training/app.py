from random import choice
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    random_name = choice(['Itgenio', 'Igor', 'Delictum'])
    project_number = 100
    return render_template('index.html',
                           name=random_name,
                           title='Home page',
                           project_number=project_number)


@app.route("/<float:num>/")
def my_route(num):
    return f"Ваше число {num}, умноженное на 2: {num * 2}"


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
