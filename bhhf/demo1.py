# coding=utf-8
# from selenium import webdriver
from selenium import webdriver

# import time
driver = webdriver.chrome()
driver.get('http://sahitest.com/demo/linkTest.htm')
# sleep(1)
# sleep(2)
driver.find_element_by_id('linkById').click()
print driver.title
