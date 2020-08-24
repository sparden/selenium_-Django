from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://localhost:8000')

assert browser.page_source.find('install')