from flask import Blueprint, render_template, redirect, url_for
from myproject import db
from myproject.models import Owner
from myproject.owners.forms import OwnerForm

owner_blueprint = Blueprint('owner', __name__, 
                            template_folder='templates/owners')

@owner_blueprint.route('/add', methods=['GET','POST'])
def owner():
    form = OwnerForm()

    if form.validate_on_submit():

        puppy_id = form.id.data
        owner_name = form.name.data

        new_owner = Owner(owner_name, puppy_id)

        db.session.add(new_owner)
        db.session.commit()

        return redirect(url_for('puppies.list_pup'))
    return render_template('owner.html', form=form)