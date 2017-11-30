# coding=utf-8

import unittest
from selenium import webdriver
from testsuit.homepage import Homepage126
from testsuit.login_page import LoginPage
import time
import os
import HTMLTestRunner
from selenium import webdriver
import sys
sys.path.append('./testsuit')
# 导入包时添加


class Test126(unittest.TestCase):

    def setUp(self):
        print "#### start test!####"
        self.driver = webdriver.Firefox()

        # driver = self.driver
        # home_page = Homepage126(driver)

    # def test_click_element(self):
    #     self.driver = webdriver.Firefox()
    #     driver = self.driver
    #     home_page = Homepage126(driver)
    #     url = 'http://www.126.com/'

    #     home_page.open(url)
    #     home_page.scrennshots()
    #     time.sleep(1)
    #     home_page.click_ad()
    #     time.sleep(2)
    #     home_page.scrennshots()

    #     # back to default window
    #     home_page.switch_to_window()
    #     #  go to 邮箱黄页
    #     home_page.click_cppage()
    #     # self.assertEqual(self.driver.title, u'网易邮箱黄页 - 国家政府机构')
    #     # back to default window
    #     home_page.switch_to_window()
    #     # click网易企业邮箱
    #     home_page.click_cpemail()
    #     # self.assertEqual(self.driver.title, u'网易企业邮箱 - 企业信息化专业解决方案', msg=None)
    #     driver.quit()　　　　　　　　　　　　　　　# 退出浏览器

    def test_login(self):
        # self.driver = webdriver.Firefox()
        # driver = self.driver
        login_page = LoginPage(self.driver)
        login_page.open('http://www.126.com/')  # 打开ｌｏｇｉｎ网页
        time.sleep(2)
        login_page.scrennshots()
        # login_page.normal_login()
        login_page.switch_frame('x-URS-iframe')  # 切换到登陆框的ｉｆｒａｍｅ　
        login_page.input_username(u'hemao1992')  # input username
        login_page.input_password(u'hemaoQ1234')  # input password
        login_page.click_login()  # click login_button

        # success　login
        # 写信


    def testadd(self):
        self.assertEqual((2 + 2), 4, msg='success!')

    def tearnDown(self):  # 注意tearnDown大写“D”
        self.driver.quit()
        print"#### end test!####"


if __name__ == '__main__':
    testunit = unittest.TestSuite()
    # testunit.addTest(Test126('test_click_element'))
    testunit.addTest(Test126('test_login'))
    testunit.addTest(Test126('testadd'))

    # file path
    imagepath = os.path.abspath('.')
    reportpath = os.path.join(imagepath, 'reports/')
    now = time.strftime('%Y-%m-%d  %H%M%S', time.localtime())
    reportfile = reportpath + now + 'report.html'
    with open(reportfile, 'wb')as f:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=f,
            title=u'网易测试报告',
            description=u'网易测试报告用例执行情况:')
        runner.run(testunit)
        f.close()
