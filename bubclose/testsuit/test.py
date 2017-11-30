# coding=utf-8
from selenium import webdriver
import unittest
import time
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Testwangyi(unittest.TestCase):

    def test1(self):

        driver = webdriver.Firefox()
        driver.get('http://www.126.com/')
        print driver.title
        self.assertEqual(driver.title, u'126网易免费邮--你的专业电子邮局')
        time.sleep(3)
        driver.switch_to.frame('x-URS-iframe')
        print "success switch to ifame!"
        # time.sleep(3)
        locator = (By.NAME, 'email')
        # user_element = EC.invisibility_of_element_located(locator)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(locator))
        #这里调用ｌｏｃａｔｏｒ必须加“*”号，不然报错,加星号相当于引用元组里的元素
        user_element = driver.find_element(*locator)
        user_element.clear()
        user_element.send_keys('hemaoq1')


if __name__ == '__main__':
    unittest.main()
