from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL


class CafeForm(FlaskForm):
    """Form class for adding a new cafe."""

    cafe = StringField('Cafe name', validators=[DataRequired()])
    location_url = StringField('Location URL', validators=[DataRequired(), URL()])
    open_time = StringField('Open Time', validators=[DataRequired()])
    close_time = StringField('Close Time', validators=[DataRequired()])

    # Choices for ratings
    RATINGS = [
        ('0', 'x'),
        ('1', '☕'),
        ('2', '☕☕'),
        ('3', '☕☕☕'),
        ('4', '☕☕☕☕'),
        ('5', '☕☕☕☕☕')
    ]

    WIFI_RATINGS = [
        ('0', 'x'),
        ('1', '💪'),
        ('2', '💪💪'),
        ('3', '💪💪💪'),
        ('4', '💪💪💪💪'),
        ('5', '💪💪💪💪💪')
    ]

    POWER_RATINGS = [
        ('0', 'x'),
        ('1', '🔌'),
        ('2', '🔌🔌'),
        ('3', '🔌🔌🔌'),
        ('4', '🔌🔌🔌🔌'),
        ('5', '🔌🔌🔌🔌🔌')
    ]

    coffee_rating = SelectField('Coffee Rating', choices=RATINGS, validators=[DataRequired()])
    wifi_rating = SelectField('Wifi Rating', choices=WIFI_RATINGS, validators=[DataRequired()])
    power_rating = SelectField('Power Rating', choices=POWER_RATINGS, validators=[DataRequired()])

    submit = SubmitField('Submit')
