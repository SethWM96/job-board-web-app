import unittest
from app import app

class TestFlaskApp(unittest.TestCase):

    def setUp(self):
        # Create a test client
        self.app = app.test_client()
        self.app.testing = True  # Set testing to True to enable exceptions to propagate to the test client

    def test_index_route(self):
        # Make a GET request to the index route
        response = self.app.get('/')

        # Assert the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if quartile_options are present in the rendered HTML content
        self.assertIn(b'Lower Quartile', response.data)
        self.assertIn(b'Middle Quartile', response.data)
        self.assertIn(b'Upper Quartile', response.data)
        self.assertIn(b'Above Upper Quartile', response.data)

if __name__ == '__main__':
    unittest.main()

