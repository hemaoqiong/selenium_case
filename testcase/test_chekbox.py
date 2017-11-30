# coding=utf-8
from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get('http://sahitest.com/demo/label.htm')
time.sleep(2)
# checkbox全选
# m = driver.find_elements_by_xpath('//input')
# for i in m:
#     i.click()
# ###
