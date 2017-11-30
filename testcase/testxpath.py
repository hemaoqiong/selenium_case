# coding=utf-8
from selenium import webdriver
import time
import unittest


class biaduTestCase(unittest.TestCase):

    def testbaidu(self):

        driver = self.driver
        driver = webdriver.Firefox()
        url_bas = 'http://www.baidu.com'
        driver.get(url_bas + '/gaoji/preferences.html')
        m = driver.find_element_by_name("NR")
    # m.find_element_by_xpath('/html/body/form/table/tbody/tr[3]/td[2]/select/option[3]').click()
        m.find_element_by_xpath('//select/option[2]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//input[@value="保存设置"]').click()
        time.sleep(2)
        driver.switch_to_alert().accept()
