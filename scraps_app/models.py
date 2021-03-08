
from sqlalchemy.orm import backref
from flask_login import UserMixin
from . import db
from . import app
import enum
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
   return User.query.get(user_id)

class User(db.Model, UserMixin):
    '''This is a user model that contains an id, username, and password, and a link to photos which is what photos have been added'''
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    photos = db.relationship(
        'Photos', secondary='user_photo', back_populates='user_added'
    )

    def __repr__(self):
        return f'<User: {self.username}>'

class Photos(db.Model):
    ''' This is a photo model to store information about the photo'''
    id = db.Column(db.Integer, primary_key = True)
    photo_name = db.Column(db.String(2000), nullable=False, unique=True )
    img_url = db.Column(db.String(200), nullable=False)
    album_id = db.Column(db.Integer, db.ForeignKey("albums.id"))
    user_added = db.relationship(
        'User', secondary='user_photo', back_populates='photos')

class Albums(db.Model):
    '''this is an album model to store info about the album'''
    id = db.Column(db.Integer, primary_key = True)
    album_name = db.Column(db.String(200), nullable=False, unique=True)
    photo_id = db.relationship("Photos", backref="photos")
    


'''This is a relationship table to link the user and photo'''
user_photo_table = db.Table('user_photo',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('photo_id', db.Integer, db.ForeignKey('photos.id'))
)



