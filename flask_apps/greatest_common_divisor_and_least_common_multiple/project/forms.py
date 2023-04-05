from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired


class TwoNumbersForm(FlaskForm):
    first_number = IntegerField('First number:', validators=[DataRequired()])
    second_number = IntegerField('Second number:', validators=[DataRequired()])
    submit = SubmitField('Calculate')
