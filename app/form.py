# Import for form
from flask_wtf import FlaskForm
from wtforms import Form, StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired


class DoubleForm(FlaskForm):
    input_nb = StringField('Input number')
    submit = SubmitField('Calculate')

class IrisForm(FlaskForm):
    sl_input = StringField('Sepal Length',[DataRequired()])
    sw_input = StringField('Sepal Width',[DataRequired()])
    pl_input = StringField('Petal Length',[DataRequired()])
    pw_input = StringField('Petal Width',[DataRequired()])
    submit = SubmitField('Predict_iris',[DataRequired()])

class BostonForm(FlaskForm):
    slc_nb_features = SelectField('nb_features',choices=["Model 1 feature","Model 2 features","Model 3 features"])

class MnistForm(FlaskForm):
    inp = "in"