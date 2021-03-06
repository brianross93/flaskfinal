
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
       

    return render_template('add_scraps.html', **context)







