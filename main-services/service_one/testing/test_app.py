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

# class TestBase(TestCase):
#     def create_app(self):
#         app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
#                 DEBUG=True,
#         return app    

#     def setUp(self):
        
#         db.create_all()

#         test_lottery = Lottery(combined_account_string="234567JJK", message_string="Congratulation you won £125", lottery=1)
#         db.session.add(test_lottery)
#         db.session.commit()
    
#     def tearDown(self):
#         db.session.remove()
#         db.drop_all()

class TestBase(TestCase):
    def create_app(self):  # creating a test base 
        return app

class TestHome(TestBase):
    def test_home(self):
        with requests_mock.mock() as m: # doing a mock of my app.py and recreating it for the test
            m.get("http://service_two:5002/numbers").text = ('3') # tested that the data/information went through
            m.get("http://service_two:5003/letters").text = ("A") # tested that the data/information went through
            response = self.client.get(url_for('home'))

    def test_view(self):
        response = self.client.get(url_for('home')) # enusring that my url works 
        self.assertIsNotNone(response.status_code, 200) # ensuring that I have a 200 status , which will show that my browser 
        self.assertIsNotNone(response.data)
    
    # def test_home_combined(self):
    #     with patch('requests.get') as f:
    #         f.return_value.text = "123456CAB"
    #         response = self.client.get(url_for('home'))
    #         self.assertIsNotNon(response.status_code, 200)
    #         self.assertIsNotNone(response.data)

