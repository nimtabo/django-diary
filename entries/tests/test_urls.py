from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ..views import entry_list, entry_detail, post_edit, post_new, post_remove, signup

class TestUrls(SimpleTestCase):

    def test_entry_list_url_resolves(self):
        url = reverse(entry_list)
        self.assertEquals(resolve(url).func, entry_list)
    
    def test_entry_detail_url_resolves(self):
        url = reverse(entry_detail, args=['1'])
        self.assertEquals(resolve(url).func, entry_detail)

    def test_post_new_url_resolves(self):
        url = reverse(post_new)
        self.assertEquals(resolve(url).func, post_new)

    def test_post_edit_url_resolves(self):
        url = reverse(post_edit, args=['1'])
        self.assertEquals(resolve(url).func, post_edit)

    def test_post_remove_url_resolves(self):
        url = reverse(post_remove, args=['1'])
        self.assertEquals(resolve(url).func, post_remove)

    def test_signup_url_resolves(self):
        url = reverse(signup)
        self.assertEquals(resolve(url).func, signup)