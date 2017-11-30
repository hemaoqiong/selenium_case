# coding=utf-8
import unittest
import os
import baidu_scrennshot
import time
import HTMLTestRunner


class Testwangyi(unittest.TestCase):
    def setup(self):
        self.driver = webdriver.Firefox()

    def tearndown(self):
        self.driver.quit()

    def test_opennews(self):
        wangpage = baidu_scrennshot.Wangyi()
        wangpage.open('http://www.126.com/')
        wangpage.scrennshots()

        time.sleep(5)
        # wangpage.click_new()
        # wangpage.scrennshots()

        wangpage.click()
        wangpage.scrennshots()
        wangpage.get_title()
        # self.assertEqual(wangpage.get_title(), u'126网易免费邮--你的专业电子邮局')


if __name__ == '__main__':
    testunit = unittest.TestSuite()
    testunit.addTest(Testwangyi('test_opennews'))

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
