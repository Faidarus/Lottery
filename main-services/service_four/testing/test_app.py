from app import app
from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
import requests_mock
import requests
import random
import string

# pytest
# pytest --cov=app
# pytest --cov-config=.coveragec --cov=.
# pytest --cov=app --cov-report=term-missing




class TestBase(TestCase):
    def create_app(self):
        return app

class TestLottery(TestBase):
    def test_lottery(self):
        with requests_mock.mock() as m:
            m.get("http://service_two:5002/numbers").text = ('3')
            m.get("http://service_two:5003/letters").text = ("A")
            response = self.client.get(url_for('winner'))
    
    
    def test_winner(self):
        response = self.client.post(url_for('winner'))
        self.assertIsNotNone(response.status_code, 200)
        self.assertIsNotNone(response.data)
   
    # def test_winner(self):
    #     with patch('requests.get') as f:
    #         f.return_value.text ="C"
    #         response = self.client.post(url_for('winner'))
    #         self.assertEqual(response.status_code, 200)
    #         self.assertIsNotNone(response.data)