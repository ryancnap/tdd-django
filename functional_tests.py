#! /usr/bin/env python

from selenium import webdriver

browser = webdriver.Firefox(60)
browser.get('http://localhost:8000')

assert 'Django' in browser.title
