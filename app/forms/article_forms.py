from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class ArticleForm(FlaskForm):
    title = StringField('Article title', validators=[DataRequired(), Length(min=10, message="Minimum 5 znaków") ])
    lead = TextAreaField('Lead', validators=[DataRequired(), Length(min=10, message="Minimum 160 znaków")])
    text = TextAreaField('Your text:', validators=[DataRequired(), Length(min=10, message="Minimum 240")])
    author = StringField('Author:', validators=[DataRequired(), Length(min=3, message="Minimum 3")])
    submit = SubmitField('Send text')

