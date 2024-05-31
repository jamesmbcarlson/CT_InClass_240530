import unittest
from faker import Faker
from app import app

fake = Faker()

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

    def test_add_nums(self):
        num1 = fake.random_number(digits=3)
        num2 = fake.random_number(digits=3)
        data = {"num1": num1, "num2": num2}
        response = self.app.post('/add', json=data)
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertEqual(data['result'], num1 + num2)

    def test_add_no_nums(self):
        data = {}
        response = self.app.post('/add', json=data)
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertEqual(data['result'], 0)

    def test_add_one_num(self):
        num1 = fake.random_number(digits=3)
        data = {"num1": num1}
        response = self.app.post('/add', json=data)
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertEqual(data['result'], num1)

    def test_get_add(self):
        response = self.app.get('/add')
        self.assertEqual(response.status_code, 405)

if __name__ == "__main__":
    unittest.main()