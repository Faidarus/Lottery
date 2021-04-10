from app import app
from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
import random
import string

class TestBase(TestCase):
    def create_app(self):
        return app

class TestLetters(TestBase):
    def test_letters(self):
        response = self.client.get(url_for('letters'))
        self.assertEqual(response.status_code, 200)

    def test_letters(self):         
        with patch('random.choice') as a:
            a.return_value = 'a'
            response = self.client.get(url_for('letters'))
            self.assertIn(b'aaaa', response.data)
        
  
