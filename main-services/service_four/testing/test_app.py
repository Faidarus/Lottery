from app import app
from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
import requests_mock
import random
import string


class TestBase(TestCase):
    def create_app(self):
        return app

class TestLottery(TestBase):
    def test_lottery(self):
        with requests_mock.mock() as m:
            m.get("http://service_two:5002/numbers").text = ('3')
            m.get("http://service_two:5003/letters").text = ("A")
            m.post("http://service_four:5001/lottery"),json = ("combined_list")
            response = self.client.get(url_for('winner')
    # def test_winner(self):
    #     response = self.client.post(url_for('winner'))
    #     self.assertEqual(response.status_code, 500)
       
   
    
  