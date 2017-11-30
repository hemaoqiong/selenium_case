# coding=utf-8
from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://mail.163.com/')
driver.implicitly_wait(20)
# driver.switch_to.frame('x - URS - iframe)
# 方式1：切换到iframe
ifr = driver.find_element_by_tag_name('iframe')
driver.switch_to.frame(ifr)
# 方式2
driver.find_element_by_name('email').clear()
driver.find_element_by_name('email').send_keys('123455')
driver.find_element_by_id('un-login').click()
driver.switch_to_default_content()
driver.find_element_by_id('theme').click()
