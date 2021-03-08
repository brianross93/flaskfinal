
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
            image=form.image.data,
            photo_name = form.photo_name.data,
            album_id = form.album_id.data
        )
        db.session.add(photo)
        db.session.commit()
        return redirect(url_for('main.display_album', photo_id=photo.album_id))
    return render_template('add_scraps.html', **context)

@main.route('/scraps_album/<photo_id>', methods=['GET', 'POST'])
def display_album(photo_id):
    """Display the web page for showing scraps in an album"""
    photo = Photos.query.get(photo_id)
    form = PhotoForm(obj=photo)
    if form.validate_on_submit():
        """If the form is valid, we want to show the added image"""
        #image, photo_name, album_id
        
        photo.image = form.image.data.filename,
        photo.photo_name = form.photo_name.data,
        photo.album_id = form.photo_name.data
        
        db.session.commit()
        
        flash('Scraps were updated successfully.')
        return redirect(url_for('main.display_album', photo_id=photo.id))


    return render_template('scraps_album.html',photo=photo, form=form)








