import unittest
from app import app

class FlaskAppTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "Welcome to the Flask App")

    def test_post_index(self):
        bad_response = self.app.post('/')
        self.assertEqual(bad_response.status_code, 405)

    