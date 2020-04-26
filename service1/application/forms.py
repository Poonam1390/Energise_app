from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError

class RoutineForm(FlaskForm):
    exercise = StringField('Exercise',
        validators = [
            DataRequired(),
            Length(min=2, max=100)
        ]
    )
    sing = StringField('Sing',
        validators = [
            DataRequired(),
            Length(min=2, max=100)
        ]
    )
    dance = StringField('Dance',
        validators = [
            DataRequired(),
            Length(min=2, max=100)
        ]
    )
    submit = SubmitField('Submit Routine!')