from app import app
from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from app import db
import requests_mock

# pytest
# pytest --cov=app
# pytest --cov-config=.coveragec --cov=.
# pytest --cov=app --cov-report=term-missing

class TestBase(TestCase):
    def create_app(self):
        return app

class TestHome(TestBase):
    def test_home(self):
        with requests_mock.mock() as m:
            m.get("http://service_two:5002/numbers").text = ('4')
            m.get("http://service_two:5003/letters").text = ("a")
            response = self.client.get(url_for('home'))

    def test_view(self):
        response = self.client.get(url_for('home'))
        self.assertIsNotNone(response.status_code, 200)
        self.assertIsNotNone(response.data)
    
    # def test_home_combined(self):
    #     with patch('requests.get') as f:
    #         f.return_value.text = "123456CAB"
    #         response = self.client.get(url_for('home'))
    #         self.assertIsNotNon(response.status_code, 200)
    #         self.assertIsNotNone(response.data)
