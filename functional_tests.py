#! /usr/bin/env python

# This one's for Travis
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		# we need to tell pyvirtualdisplay to start;
		# we would't have to do this if it weren't for Travis.
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
		# TRAVIS: the below three lines will also fail on Travis.
		# HAHA NOT ANYMORE FUCK YOU TRAVIS
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)

		# You are invited to enter a to-do item straight away.
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item'
			)

		# You enter 'Buy peacock feathers' into a text box
		inputbox.send_keys('Buy peacock feathers')

		# When you hit enter, the page updates and now lists
		# 1: Buy peacock feathers as an item in a to-do list table.
		inputbox.send_keys(Keys.ENTER)

		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn('1: Buy peacock feathers', [row.text for row in rows])

		# There is still a text box inviting you to add another item.
		self.fail('Finish the test!')

if __name__ == '__main__':
	unittest.main()