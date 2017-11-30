# coding=utf-8
from selenium import webdriver
from time import sleep

# from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
base_url = 'http://60.205.169.195:7060/'
driver.get(base_url)
sleep(2)
# driver.quit()
m = driver.find_element_by_xpath(
    '/html/body/header/div/div[1]/div/div[2]/span[1]/a')
m.click()
sleep(2)
driver.find_element_by_class_name('inputTel').clear()
driver.find_element_by_class_name('inputTel').send_keys('17828770886')

# driver.find_element_by_xpath(u"//input[@value='获取验证码']").click()
# driver.find_element_by_css_selector("input.inputTel").clear()
# driver.find_element_by_css_selector(
#     "input.inputTel").send_keys("17828770886")

driver.find_element_by_class_name('get_vertificate_code').click()
driver.find_element_by_class_name('input_vertificate_code').clear()
sleep(5)
'''u'输入验证码'''
# 手动输入验证码
driver.find_element_by_class_name('checkbox_btn').click()

driver.find_element_by_id('login_btn').click()
'''
登录
'''
