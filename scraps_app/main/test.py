import os
import unittest

from datetime import date
 
from scraps_app import app, db, bcrypt
from scraps_app.models import User

'''This is the setup for the tests. Helper function
    However, tests are not functional yet
'''

def login(client, username, password):
    return client.post('/login', data=dict(
        username=username,
        password=password
    ), follow_redirects=True)
'''This is the setup for the tests which sets up logout. This is a helper function'''
def logout(client):
    return client.get('/logout', follow_redirects=True)
'''This is the setup for the tests which creates a user. Helper Function'''
def create_user():
    # Creates a user with username 'me1' and password of 'password'
    password_hash = bcrypt.generate_password_hash('password').decode('utf-8')
    user = User(username='me1', password=password_hash)
    db.session.add(user)
    db.session.commit()

#tests
def test_homepage_logged_in(self):
        """Test that the things show up on the homepage."""
      
        create_user()
        login(self.app, 'me1', 'password')

        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        # Make a GET request
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        # Check that page contains all of the things we expect
        response_text = response.get_data(as_text=True)
        
        self.assertIn('me1', response_text)
        

        # Check that the page doesn't contain things we don't expect
        # (these should be shown only to logged out users)
        self.assertNotIn('Log In', response_text)
        self.assertNotIn('Sign Up', response_text)


def test_logged_out(self):
        """Test that the things appears on its detail page."""
       
        create_user()
       
       
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

       
        response_text = response.get_data(as_text=True)
        self.assertIn('me2', response_text)
        

     

        self.assertNotIn('Favorite', response_text)

def test_logout(self):
        create_user()

        post_data = {
            'username': 'me2',
            'password': 'password'
        }
        self.app.post('/logout', follow_redirects=True)
        homepage_text = logged_out.get_data(as_text=True)

        self.assertIn("Log In", homepage_text)