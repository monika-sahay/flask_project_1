from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField


class AddForm(FlaskForm):

    name = StringField('Name of the puppy: ')
    submit = SubmitField('Add puppy')


class DelForm(FlaskForm):

    id = IntegerField('Id Number of puppy to remove')
    submit = SubmitField('Remove')


