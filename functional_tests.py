#! /usr/bin/env python

from pyvirtualdisplay import Display
from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		display = Display(visible = 0, size=(800, 600))
		display.start()

		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		# You hear about an online app and go check it's homepage.
		self.browser.get('http://localhost:8000')

		# You notice the page title and header mention todo lists.
		self.assertIn('To-Do', self.browser.title)
		self.fail('Remember to finish this test.')

		# You are invited to enter a to-do item straight away.
		# rest of test, comments, etc.

if __name__ == '__main__':
	unittest.main(warnings='ignore')