# coding=utf-8
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from seleniuml.webdriver.support.ui import
# from seleniuml.common.exceptions import ElementNotvisibleException
from selenium import webdriver
from seleniuml.webdriver.common.action_chains import ActionChains
import time
import unittest


class ATestCase(unittest.TestCase):
    def setup(self):
        self.driver = webdriver.firefox()
        self.driver.get('http://www.baidu.com')

    def testa():
        driver = self.driver
        sleep(1)
        ele = driver.find

if __name__ == '__main__':
    unittest.main()
