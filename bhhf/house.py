# coding=utf-8
from selenium import webdriver
from time import sleep
# from selenium.webdriver.common.action_chains import ActionChains
# import unittest


# class HouseTestcase(unittest.TestCase):

def testLogin():
    driver = webdriver.Firefox()
    base_url = 'http://60.205.169.195:8001/#/login?_k=76pwx2'
    driver = driver
    driver.get(base_url)
    sleep(2)
    driver.find_element_by_name('username').clear()
    driver.find_element_by_name('username').send_keys('N000103')
    driver.find_element_by_name('password').clear()
    driver.find_element_by_name('password').send_keys('123456')
    driver.find_element_by_xpath('//button[1]').click()  # 使用xpath定位button
    # print driver.currunt_url()


if __name__ == "__main__":
    testLogin()

    # driver.quit()
