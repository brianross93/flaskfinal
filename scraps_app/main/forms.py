from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField, SelectField, SubmitField, TextAreaField
from wtforms.ext.sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, Length, ValidationError
from scraps_app.models import *


class PhotoForm(FlaskForm):
    '''This is a Photo form where people can upload photos'''
    image = FileField("Image", validators=[FileAllowed(["jpg", "png"])])
    photo_name = StringField('Photo Name',
        validators=[DataRequired()])
    album_id = StringField("Album ID",validators=[Length(min=3, max=50)] )
    submit = SubmitField("Add Photo")

class AlbumForm(FlaskForm):
    '''This is an album form for users to utilize'''
    album_name = StringField("Album Name", validators=[DataRequired(), Length(min=3, max=80)] )



