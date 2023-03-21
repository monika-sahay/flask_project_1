from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class OwnerForm(FlaskForm):
    
    id = IntegerField('Id Number of the pup')
    name = StringField('Name of the owner')
    submit = SubmitField('Add owner')
