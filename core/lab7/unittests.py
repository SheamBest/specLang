import unittest
from .API.api import APIClient, parse_input

class TestAPIClient(unittest.TestCase):
    def setUp(self):
        self.client = APIClient('https://jsonplaceholder.typicode.com')

    def test_get_posts(self):
        posts = self.client.get('/posts')
        self.assertIsInstance(posts, list)
        self.assertTrue(len(posts) > 0)
        for post in posts:
            self.assertIsInstance(post, dict)
            self.assertIn('userId', post)
            self.assertIn('id', post)
            self.assertIn('title', post)
            self.assertIn('body', post)
    
    def test_parse_input(self):
        self.assertEqual(parse_input("01-01-2020"), ["01-01-2020"])
        self.assertEqual(parse_input("The date is 01-01-2020."), ["01-01-2020"])
        self.assertEqual(parse_input("No date here"), [])

def main():
    test_lab7 = unittest.TestLoader().loadTestsFromTestCase(TestAPIClient)
    test_loader = unittest.TextTestRunner()

    test_loader.run(test_lab7)
    input()

if __name__ == '__main__':
    main()