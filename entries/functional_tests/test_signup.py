# from django.contrib.staticfiles.testing import LiveServerTestCase
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from django.urls import reverse
# from ..models import Entry
# import time


# class TestEntriesListPage(LiveServerTestCase):

#     def setUp(self):
#         self.browser = webdriver.Chrome(ChromeDriverManager().install())

#     def tearDown(self):
#         self.browser.close()

#     def test_welcome_message_is_displayed(self):
#         self.browser.get('%s%s' % (self.live_server_url, '/accounts/singup/')) #(self.live_server_url) '%s%s' % (self.live_server_url, '/login/')

#         # user request page for the first time
#         text = self.browser.find_element_by_tag_name('h2')
#         self.assertEquals(text.text, 'Create account')

#     # def test_create_account_button_redirect_to_signup(self):
#     #     self.browser.get(self.live_server_url)

#     #     # user redirected to signup page
#     #     signup_url = self.live_server_url + reverse('signup')
#     #     self.browser.find_element_by_tag_name('button').find_element_by_tag_name('a').click()
#     #     self.assertEquals(
#     #         self.browser.current_url,
#     #         signup_url
#     #     )