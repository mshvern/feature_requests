from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.fields.html5 import DateField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange


class FeatureRequestForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=256)])
    description = TextAreaField('Description', validators=[DataRequired()])
    client = SelectField('Client', validators=[DataRequired()], coerce=int)
    client_priority = IntegerField('Client Priority', validators=[DataRequired(), NumberRange(min=1)])
    target_date = DateField('Target Date', validators=[DataRequired()])
    product_area = SelectField('Product Area', validators=[DataRequired()], coerce=int)
    submit = SubmitField('Send')
