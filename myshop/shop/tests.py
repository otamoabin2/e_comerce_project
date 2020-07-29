# users/tests.py
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve
from django.test import SimpleTestCase
from django.urls import reverse, resolve

from .views import HomePageView, AboutPageView

class HomepageTests(SimpleTestCase):
    pass 

class AboutPageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('about_us')
        self.response = self.client.get(url)

    def test_aboutpage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_aboutpage_template(self):
        self.assertTemplateUsed(self.response, 'about_us.html')

    def test_aboutpage_contains_correct_html(self):
        self.assertContains(self.response, 'about')

    def test_aboutpage_does_not_contain_incorrect_html(self):
        self.assertNotContains(
            self.response, 'Hi there! I should not be on the page.')
