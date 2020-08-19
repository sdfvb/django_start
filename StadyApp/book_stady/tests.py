from django.test import TestCase, SimpleTestCase
from django.urls import reverse


class BookpageTests(SimpleTestCase):

    def test_home_page_code(self):
        response = self.client.get('/book/')
        self.assertEqual(response.status_code, 200)

    # def test_home_page_url_name(self):
    #     response = self.client.get(reverse('book'))
    #     self.assertEqual(response.status_code, 200)

    def test_home_page_template(self):
        response = self.client.get('/book/')
        self.assertTemplateUsed(response, 'home_page.html')