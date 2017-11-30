# coding=utf-8
from selenium import webdriver
import time
import HTMLTestRunner
import unittest


class Baidu(unittest.TestCase):
    def baidutest(self):
        driver = self.driver
        driver = webdriver.Firefox()
        driver.get('http://www.baidu.com')
        driver.find_element_by_id('kw').send_keys('selenium')
        driver.find_element_by_id('su').click()
        time.sleep(3)

        js = 'var q=document.documentElement.scrollTop=10000'
        driver.execute_script(js)
        time.sleep(3)
        js = 'var q=document.documentElement.srollTop=0'

        driver.execute_script(js)
        time.sleep(3)

        driver.quit()
        if _name_ == '_main_':
            # filename='/home/forin/result.html'
            #f=file(filename, 'wb')
            #run=HTMLTestRunner.main(module='__main__', defaultTest=None, argv=None, testRunner=None, testLoader=loader.defaultTestLoader, exit=True, verbosity=1, failfast=None, catchbreak=None, buffer=None)
            HTMLTestRunner.main()
