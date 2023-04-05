from flask import Flask, render_template
from game_of_life import GameOfLife


app = Flask(__name__)


@app.route('/')
def index():
    GameOfLife(width=20, height=18)
    return render_template('index.html')


@app.route('/live')
def live():
    running_game_of_live = GameOfLife()
    running_game_of_live.form_new_generation()
    return render_template('live.html', running_game_of_live=running_game_of_live)


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
