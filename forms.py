from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField
from wtforms.validators import DataRequired 

class TodoForm(FlaskForm):
    title=StringField('Tytuł', validators=[DataRequired()])
    description=BooleanField('Opis', validators=[DataRequired()])
    done=TextAreaField('Czy zrobione?', validators=[DataRequired()])