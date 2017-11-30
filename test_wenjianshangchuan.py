# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get('http://sahitest.com/demo/php/fileUpload.htm')
upload = driver.find_element_by_id('file')
upload.send_keys('/home/forin/WorkSpace/data.txt')

sleep(3)
# send_keys
print upload.get_attribute('value')  # check value

driver.quit()
