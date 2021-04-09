from app import app
from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
import random
import string


class TestBase(TestCase):
    def create_app(self):
        return app

class TestLottery(TestBase):
    def test_winner(self):
        response = self.client.post(url_for('lottery'))
        self.assertEqual(response.status_code, 200)
       
   
    
  