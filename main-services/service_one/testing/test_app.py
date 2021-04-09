from app import app
from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
import requests_mock


class TestBase(TestCase):
    def create_app(self):
        return app

class TestHome(TestBase):
    def test_home(self):
        with requests_mock.mock() as m:
            m.get("http://service_two:5002/numbers").text = ('3')
            m.get("http://service_two:5003/letters").text = ("A")
            # m.post("http://service_four:5001/lottery").json = ("new_winner")
            response = self.client.get(url_for('home'))
            # self.assertIn(b'A', response.data)

    def test_home(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 500)
