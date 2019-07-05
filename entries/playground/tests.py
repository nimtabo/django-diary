import unittest
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.utils import timezone

from .views import entry_detail, entry_list, post_edit, post_new, post_remove, signup
from .models import Entry

# test views


class ViewsTest(TestCase):
    def setUp(self):
        """every test needs access to the request factory"""
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='chacha',
                                             email='chacha@gmail.com', password='mypasswd')

        # seed entry
        title = 'title'
        text = 'text'
        author = self.user
        self.entry = Entry.objects.create(title=title, text=text, author=author,
                                          created_date=timezone.now())

    def test_list_entry_status_code(self):
        """ Test Home page/ Dashboard loads """

        request = self.factory.get('/')

        # logged-in user
        request.user = self.user

        # test view
        response = entry_list(request)
        # response = entry_list.as_view()(request)
        self.assertEqual(response.status_code, 200)

    # #

    def test_entry_details(self):
        # create entry
        """ Test details page loads with correct id """
        request = self.factory.get('entry/{}/'.format(self.entry.id))
        request.user = self.user
        response = entry_detail(request, self.entry.id)
        self.assertEqual(response.status_code, 200)

    def test_render_post_new_entry_form(self):
        """ Test new entry form loads with no errors """

        request = self.factory.get('entry/new/')
        request.user = self.user
        response = post_new(request)
        self.assertEqual(response.status_code, 200)

    def test_post_new_entry_with_empty_form(self):
        """ Test post_new cannot post with empty form """

        request = self.factory.post('entry/new/', {'title': 'title', 'text': 'text'})
        request.user = self.user
        response = post_new(request)
        self.assertNotEqual(response.status_code, 200)
        