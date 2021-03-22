# Import for form
from flask_wtf import FlaskForm
from wtforms import Form, StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class DoubleForm(FlaskForm):
    input_nb = StringField('Input number')
    submit = SubmitField('Calculate')

class IrisForm(FlaskForm):
    sl_input = StringField('Sepal Length')
    sw_input = StringField('Sepal Width')
    pl_input = StringField('Petal Length')
    pw_input = StringField('Petal Width')
    submit = SubmitField('Predict_iris')