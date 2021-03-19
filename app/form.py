# Import for form
from flask_wtf import FlaskForm
from wtforms import Form, StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class DoubleForm(FlaskForm):
    input_nb = StringField('Input number')
    submit = SubmitField('Calculate')