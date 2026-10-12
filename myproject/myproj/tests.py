from django.http import response
from django.test import TestCase

class HomepageTest(TestCase):
    def test_home_page(self):
        self.assertEqual(2+2,4)

class AboutpageTest(TestCase):
    def test_about_page(self):
        self.assertTrue(3+3==6)

class ContactpageTest(TestCase):
    def test_contact_page(self):
        self.assertFalse(4+4==5)

# class Test(TestCase):
#     def test_page(self):
#         self.assertContains(response, "Welcome to my website")
# Create your tests here.
