# coding=utf-8
import selenium
import time
import unittest


def Bugclose(unittest.TestCase):

    def test_lofin():
        driver = webdriver.Firefox()
        driver.get('https://www.bugclose.com/login.html')
        m = driver.find_element_by_name('email')
        m.clear()
        m.send_keys('2447617382@qq.com')
        p = driver.find_element_by_name('password')
        p.clear()
        p.send_keys('HEMAOQIONG123')
        driver.find_element_by_xpath(
            '/html/body/div[2]/div/form/div[3]/i').click()
        driver.find_element_by_id('loginBtn').click()
        assert 'bugclose' in driver.title
    def test_page():
