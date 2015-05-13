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

	# Add a helper method; only methods starting with _test will be run.
	def check_for_row_in_list_table(self, row_text):
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn(row_text, [row.text for row in rows])

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
		self.check_for_row_in_list_table('1: Buy peacock feathers')

		# There is still a text box inviting you to add another item.
		# You enter 'Use peacock feathers to make a fly'
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Use peacock feathers to make a fly')
		inputbox.send_keys(Keys.ENTER)

		# The page updates again, and now shows both items on the list.
		self.check_for_row_in_list_table('1: Buy peacock feathers')
		self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

		# You wonder whether the site will remember your list. Then you see
		# that the site has generated a unique url for you.

		self.fail('Finish the test!')

if __name__ == '__main__':
	unittest.main()