#! /usr/bin/env python

from selenium import webdriver

# this section added to satisfy Travis
# enabless headless firefox
# pyvirtualdisplay is a python wrapper for xvfb
from pyvirtualdisplay import Display

display = Display(visible = 0, size=(800, 600))
display.start()

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'Django' in browser.title

# always fill your divits
browser.close()
display.stop()