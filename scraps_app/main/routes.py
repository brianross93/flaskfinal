
from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from datetime import date, datetime
from .. import app
from scraps_app.models import User, Photos
from scraps_app.main.forms import PhotoForm
from scraps_app import app, db




main = Blueprint("main", __name__)




@main.route('/')
def home():
    """Display the web page for home"""
    # new_user = User(username='me1', password='Casirus')
    # db.session.add(new_user)
    # db.session.commit()
    # print(new_user)
    return render_template('index.html')

@main.route('/albums')
def albums():
    """Display the web page for albums"""
    return render_template('albums.html')

@main.route('/add_album')
def add_album():
    """Display the web page for adding albums"""
    return render_template('add_album.html')

@main.route('/add_scraps', methods=['POST', 'GET'])
def add_scraps():
    """Display the web page for adding scraps/photos"""
    form = PhotoForm()
    context = {
        'form':form
    }
    if form.validate_on_submit():
        
        photo = Photos(
            img_url=form.image.data,
            photo_name = form.photo_name.data,
            album_id = form.album_id.data
        )
        db.session.add(photo)
        db.session.commit()
        print("Hello here i am step 1")
        return redirect(url_for('main.display_album', photo_id=photo.id))
    return render_template('add_scraps.html', **context)

@main.route('/scraps_album/<photo_id>', methods=['GET', 'POST'])
def display_album(photo_id):
    """Display the web page for showing scraps in an album"""
    photo = Photos.query.get(photo_id)
    print(photo)
    form = PhotoForm(obj=photo)
    print(form)
    print("we got to the display album route")
    if form.validate_on_submit():
        print("the form is valid")
        #image, photo_name, album_id
        image = form.image.data.filename,
        photo_name = form.photo_name.data,
        album_id = form.photo_name.data

        db.session.commit()
        flash('Scraps were updated successfully.')
        return redirect(url_for('main.display_album', photo_id=photo.id))


    return render_template('scraps_album.html')

# @main.route('/item/<item_id>', methods=['GET', 'POST'])
# def item_detail(item_id):
#     item = GroceryItem.query.get(item_id)
#     # Creates a GroceryItemForm and pass in `obj=item`
#     form = GroceryItemForm(obj=item)

#     # If form was submitted and was valid:
#     # - update the GroceryItem object and save it to the database,
#     # - flash a success message, and
#     # - redirect the user to the item detail page.
#     if form.validate_on_submit():
#         new_item = GroceryItem(
#             name=form.name.data,
#             price=form.price.data,
#             category=form.category.data,
#             photo_url=form.photo_url.data,
#             store=form.store.data
#         )

#         db.session.add(new_item)
#         db.session.commit()

#         flash('New item created')
#         return redirect(url_for('main.item_detail', item_id=new_item.id))

#     #  Sends the form to the template and use it to render the form fields
#     item = GroceryItem.query.get(item_id)
#     return render_template('item_detail.html', item=item)







