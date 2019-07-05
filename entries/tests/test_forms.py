from django.test import TestCase
from ..forms import EntryForm, SignUpForm


class TestForms(TestCase):

    def test_entry_form_with_valid_data(self):
        ''' test entry form with valid data '''
        form = EntryForm(data={
            'title': 'title x',
            'text': 'texts'
        })

        self.assertTrue(form.is_valid())

    def test_entry_form_with_no_data(self):
        ''' test entry form with no or invalid data '''
        form = EntryForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)

    def test_signup_form_with_valid_data(self):
        ''' test signup form with valid data '''
        form = SignUpForm(data={
            'username': 'nic',
            'first_name': 'nicholas',
            'last_name': 'nicklas',
            'email': 'nich@mail.net',
            'password1': 'verysecrete',
            'password2': 'verysecrete'
        })

        self.assertTrue(form.is_valid())

    def test_signup_form_with_no_data(self):
        ''' test signup form with no or invalid data '''
        form = SignUpForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)
