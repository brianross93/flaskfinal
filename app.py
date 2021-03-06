import jinja2
from flask import Flask, request, redirect, render_template, url_for
import os
import pytz
import requests
import sqlite3
from pprint import PrettyPrinter
from datetime import datetime, timedelta
from dotenv import load_dotenv
from flask import Flask, render_template, request, send_file
from flask_sqlalchemy import SQLAlchemy
from scraps_app.models import User, Photos

from scraps_app import app

if __name__ == "__main__":
    app.run(debug=True)

'''This runs the app'''
app = Flask(__name__, template_folder="templates")
load_dotenv()
db = SQLAlchemy(app)



