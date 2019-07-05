from django.test import TestCase, Client
from django.contrib.auth.models import User
from ..models import Entry

class TestModels(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='chacha',
                    email='chacha@gmail.com', password='mypasswd')
        self.entry = Entry.objects.create(
            title='title',
            text='test text',
            author= self.user
        )
    def test_moedl_created_with_all_fields(self):
        self.assertEquals(self.entry.title, 'title')
        self.assertEquals(self.entry.text, 'test text')

        # test model created by loged in user
        self.assertEquals(self.entry.author, self.user)