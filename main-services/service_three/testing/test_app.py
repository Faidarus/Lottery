from app import app
from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
import random
import string

class TestBase(TestCase): # creating a test base
    def create_app(self):
        return app

class TestLetters(TestBase):
    def test_letters(self):  
        response = self.client.get(url_for('letters'))
        self.assertEqual(response.status_code, 200) # testing the 200 status and ensurig that it means redirecting properly

    def test_letters(self):         
        with patch('random.choice') as a:   # patch test to recreate the app functiom
            a.return_value = 'A'
            response = self.client.get(url_for('letters'))
            self.assertIn(b'AAA', response.data)
        
  
