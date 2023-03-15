from app import app, db, Puppy
from flask_sqlalchemy import SQLAlchemy

### create
app.app_context().push()
my_puppy = Puppy('Rufus', 5)
new_puppy = Puppy('Frankie', 11)
db.session.add(my_puppy)
db.session.add(new_puppy)
db.session.commit()

## read

all_puppies = Puppy.query.all()
print(all_puppies)

## select by ID
puppy_one = Puppy.query.get(1)
print(puppy_one.name)

### select by filter

puppy_franckie = Puppy.query.filter_by(name='Frankie')
print(puppy_franckie.all())


### update
first_puppy = Puppy.query.get(1)
first_puppy.age = 10
db.session.add(first_puppy)
db.session.commit()

## delete
second_puppy = Puppy.query.get(2)
db.session.delete(second_puppy)
db.session.commit()
# session = Session()
# print(session.get())
all_puppies = Puppy.query.get(1)
print(all_puppies)