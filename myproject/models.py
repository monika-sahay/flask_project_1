# setup db inside the __init__.py under myproject folders
from myproject import db


class Puppy(db.Model):
    __tablename__ = 'puppies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    owner = db.relationship('Owner', backref='puppies')
    # age = db.Column(db.Integer)

    def __init__(self,name):
        self.name = name

    def __repr__(self):

        if self.owner:
            return f'puppy owner is {self.owner.name}'
        return f'puppy name: {self.name} | puppy id: {self.id}'


class Owner(db.Model):
    __tablename__ = "owners"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer, db.ForeignKey('puppies.id'))

    def __init__(self, name, puppy_id):
        self.name = name
        self.puppy_id = puppy_id