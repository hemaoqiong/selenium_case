# coding=utf-8
from selenium import webdriver
import os
import time

source = open('/home/forin/WorkSpace/data.txt', 'r')
value = source.readlines()
source.close()

for seach in value:
    driver = webdriver.Firefox()
    driver.get('http://www.baidu.com')
    time.sleep(3)
    driver.find_element_by_id('kw').send_keys(seach)
    driver.find_element_by_id("su").click()
    time.sleep(3)
