##################################################
############# Crreaating models ##################
##################################################
##################################################
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)
Migrate(app, db)


class Puppy(db.Model):
    # Manual table name choice
    __tablename__ = 'puppies'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    ## One to many
    ## Puppy to many toys......
    toys = db.relationship('Toy', backref='puppy', lazy='dynamic')
    ## One to One
    ## One puppy --- one ownner
    owner = db.relationship('Owner', backref='puppy', uselist=False)

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'name:{self.name}| age:{self.age}'


    def report_toys(self):
        print('Here are my toys')
        for toy in self.toys:
            print(toy.item_name)


class Toy(db.Model):
    __tablename__ = 'toys'

    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer, db.ForeignKey('puppies.id'))

    def __init__(self, item_name, puppy_id):
        self.item_name = item_name
        self.puppy_id = puppy_id



class owner(db.Model):
    __tablename__ = 'owners'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)

    puppy_id = db.Column(db.Integer, db.ForeignKey('puppies.id'))

    def __init__(self, name, puppy_id):
        self.name = name
        self.puppy_id = puppy_id

    


##################################################
############# connecting to data base ############
##################################################
##################################################
# import os
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

# basedir = os.path.abspath(os.path.dirname(__file__))

# app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
# app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

# db = SQLAlchemy(app)
# Migrate(app, db)
# #----------------------------------------------------flask----------------------------#

# class Puppy(db.Model):

#     # Manual table name choice
#     __tablename__ = 'puppies'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.Text)
#     age = db.Column(db.Integer)
#     breed = db.Column(db.Text)

#     def __init__(self, name, age, breed):
#         self.name = name
#         self.age = age
#         self.breed = breed

#     def __repr__(self):
#         return f'Puppy {self.name} is {self.age} year/s old'





##################################################
##################################################
############# FLASK FORM #########################
##################################################
##################################################


# from flask import Flask, render_template,flash, session, redirect, url_for
# from flask_wtf import FlaskForm
# from wtforms import (StringField, BooleanField, DateTimeField, 
#                     RadioField, SelectField,
#                     TextAreaField, SubmitField)

# from wtforms.validators import DataRequired

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'mysecretkey'

# class InfoForm(FlaskForm):

#     breed = StringField('What field are you?', validators=[DataRequired()])
#     neutered = BooleanField("have you been neutered")
#     mood = RadioField('Please chose your mood',
#                         choices=[('mood_one','happy'), ('mood_two', 'excited')])

#     food_choice = SelectField(u'Pick your favorite Food:',
#                             choices=[('chi', 'chicken'),('bf', 'beef')])

#     feedback = TextAreaField()

#     submit = SubmitField('Submit')



# @app.route('/', methods=['GET','POST'])
# def index():
#     form = InfoForm()

#     if form.validate_on_submit():
#         session['breed'] = form.breed.data
#         session['neutered'] = form.neutered.data
#         session['mood'] = form.mood.data
#         session['food_choice'] = form.food_choice.data
#         session['feedback'] = form.feedback.data
#         flash('you just clicked the button') 

#         return redirect(url_for('thankyou'))

#     return render_template('index.html', form=form)


# @app.route('/thankyou')
# def thankyou():
#     return render_template('thankyou.html')










# from flask import Flask, render_template, request
# from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField

# app = Flask(__name__)

# app.config['SECRET_KEY'] = 'mysecretkey'

# class InfoForm(FlaskForm):
#     breed = StringField('What breed ar you?')
#     sumbit = SubmitField('Submit')

# @app.route('/form', methods=['GET','POST'])
# def form_view():
#     breed = False
#     form = InfoForm()

#     if form.validate_on_submit():
#         breed = form.breed.data
#         form.breed.data = ''

#     return render_template('form.html', form=form, breed=breed)


# @app.route('/')  # http://ec2-3-86-98-236.compute-1.amazonaws.com:8080/  gunicorn -b 0.0.0.0:8080 app:app
# def index():
#     return render_template('home.html')

# @app.route('/signup_for')
# def signup_form():
#     return render_template('signup.html')


# @app.route('/thankyou')
# def thank_you():
#     first = request.args.get('first')
#     last = request.args.get('last')
#     return render_template('thankyou.html', first=first, last=last)

# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template('404.html'), 404

# @app.route('/username')
# def username():
#     # username = request.args.get('username')
#     return render_template('username.html')

# @app.route('/check')
# def check():
#     lower_letter = False
#     upper_letter = True
#     num_end = False
#     username = request.args.get('username')
#     lower_letter = any(c.islower() for c in username)
#     upper_letter = any(c.isupper() for c in username)
#     num_end = username[-1].isdigit()
#     check = lower_letter and upper_letter and num_end
#     return render_template('check.html', check=check, lower=lower_letter,
#                             upper=upper_letter, num=num_end)


# @app.route('/')  # http://ec2-3-86-98-236.compute-1.amazonaws.com:8080/
# def index():
#     return render_template('home.html')

# @app.route('/puppy/<name>')
# def pup_name(name):
#     return render_template('puppy.html',name=name)


#@app.route('/')  # http://ec2-3-86-98-236.compute-1.amazonaws.com:8080/
# def index():
#     name = 'Moni'
#     letters = ['Moni', 'Pritesh', 'Sweeky', 'Ravi', 'ryansh']
#     pic_dict = {'ganish': 'son of shiva'}
#     return render_template('basic.html', name=name, letters=letters
#                             ,pic_dict=pic_dict)












if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)