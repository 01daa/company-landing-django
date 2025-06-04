# main/tests.py

from django.test import TestCase

class HomePageTest(TestCase):
    def test_home_page_returns_200(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
