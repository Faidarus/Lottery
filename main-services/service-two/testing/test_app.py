from unittest.mock import patch
from flask_testing import TestCase


class TestBase(TestCase):
    def create_app(self)
    return app

class TestNumbers(TestBase):
    def test_numbers(self):
        response = self.client.data(url("numbers"))
        self.assert(len(response.text), 5)

with patch('empty_list') as f:
    f.return_value = [10, 5, 3, 7, 5, 4]