from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class NameForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(),Length(max=15, message="Name too long")])
    submit = SubmitField('Play')