from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField


class AddForm(FlaskForm):

    name = StringField('Name of the puppy: ')
    submit = SubmitField('Add puppy')


class DeleteForm(FlaskForm):

    id = IntegerField('Id Number of puppy to remove')
    submit = SubmitField('Remove')

class OwnerForm(FlaskForm):
    
    id = IntegerField('Id Number of the pup')
    name = StringField('Name of the owner')
    submit = SubmitField('Add owner')

