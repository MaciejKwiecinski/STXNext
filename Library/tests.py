from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse,resolve
from .views import BookListView, main
from .api.views import DocsView,BooksApiView
import json
# I think if i will show you test of every part, it will be enough.

class TestUrls(SimpleTestCase):
    def test_booklist(self):
        url = reverse('booklist')
        self.assertEquals(resolve(url).func.view_class,BookListView)

    def test_apilist(self):
        url = reverse('apilist')
        self.assertEquals(resolve(url).func.view_class,DocsView)

    def test_apibooklist(self):
        url = reverse('apibooklist')
        self.assertEquals(resolve(url).func.view_class, BooksApiView)

    def test_main(self):
        url = reverse('main')
        self.assertEquals(resolve(url).func, main)

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()

    def test_AddBookView(self):
        response = self.client.get(reverse(('addbook')))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'addbook.html')

