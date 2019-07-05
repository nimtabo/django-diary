from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from ..models import Entry
import json


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_url = reverse('entry_list')
        self.detail_url = reverse('entry_detail', args=['1'])
        self.user = self.user = User.objects.create_user(username='chacha',
                                             email='chacha@gmail.com', password='mypasswd')
        self.entry = Entry.objects.create(title='title', text='test text', author=self.user)
        self.post_new_url = reverse('post_new')
        self.post_edit_url = reverse('post_edit', args=['1'])
        self.post_delete_url = reverse('post_remove', args=['1'])


    def test_entry_list_GET(self):
        response = self.client.get(self.list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'entries/entry_list.html')

# ==========================ERR
    # def test_entry_detail_GET(self):
    #     response = self.client.get(self.detail_url)

    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'entries/entry_detail.html')

    def test_post_new_GET(self):
        response = self.client.get(self.post_new_url)

        self.assertEquals(response.status_code, 302)
        self.assertTemplateNotUsed(response, 'entries/post_edit.html')

    def test_post_new_POST(self):
        # Entry.objects.create(
        #     title='title',
        #     text='text2',
        # )

        response = self.client.post(self.post_new_url, {
            'title': 'title',
            'text': 'text tests',
        })


        self.assertEquals(response.status_code, 302)
        self.assertTemplateNotUsed(response, 'entries/post_edit.html')
        self.assertEquals(self.entry.title, 'title')

    def test_post_edit_GET(self):
        response = self.client.get(self.post_edit_url)

        self.assertEquals(response.status_code, 302)
        self.assertTemplateNotUsed(response, 'entries/post_edit.html', json.dumps({
            'id': 1
        }))

# =======================================================================================
    # def test_post_DELETE(self):
        # new_entry = Entry.objects.create(title='mytitle', text='test text', author=self.user)
        # response = self.client.delete(self.post_delete_url)

        # self.assertEquals(response.status_code, 302)
        # self.assertEquals(new_entry.text, '')