from math import gcd, lcm

from flask import Flask, render_template, redirect

from config import Config
from project.forms import TwoNumbersForm

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/', methods=['GET', 'POST'])
def index():
    form = TwoNumbersForm()
    if form.validate_on_submit():
        a = form.first_number.data
        b = form.second_number.data
        return redirect('/calculate/' + str(a) + '/' + str(b)+ '/')
    return render_template('index.html', form=form)


@app.route('/calculate/<int:a>/<int:b>/')
def calculate(a, b):
    return render_template(
        'generated_gcd_and_lcm.html', calculated_gcd=gcd(a, b), calculated_lcm=lcm(a, b), zip=zip
    )


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
