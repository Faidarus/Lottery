from unittest.mock import patch
from flask_testing import TestCase

class TestBase(TestCase):
    def create_app(self)
    return app

class TestLetters(TestBase):
    def test_letters(self):
        response = self.client.data(url("letters"))
        self.assert(len(response.text), L)
        
          
with patch('empty_letter_list') as a:
    a.return_value = ['DYJJOVLW']
