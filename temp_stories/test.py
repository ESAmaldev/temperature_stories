from django.test import Client, TestCase
from .views import convert

# Create your tests here.

class TemperatureTests(TestCase):
  def test_story_test(self): # convention function start with test
    client = Client()
    response=client.get('/') # '/' go to root to check if there is a response
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, 'into conflict with')

  def test_convert(self):
    self.assertEqual(100.008, convert(212))