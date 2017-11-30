
# coding=utf-8
import unittest
import os
import time
from package.common import config
from pages.baidu_homepage import Homepage
from selenium import webdriver
import HTMLTestRunner


class Test_search(unittest.TestCase):
    def setup(self):
        driver = webdriver.Firefox()
        self.driver = driver
        self.url = "https://www.baidu.com"
        text = 'yoyo'

    def tearndown(self):
        self.driver.quit()

    def test_baidu():
        home = Homepage()
        home.open(self.url)
        home.input_keys(text)
        home.submmit()

        # suit = unittest.TestSuite(tests=(test_baidu))
    def run():

        path = os.path.abspath('.')
        path1 = os.path.join(path, "package")
        filepath = path1 + '/reports/'
    # 获取系统当前时间
        now = time.strftime('%Y%m%d%M%H%S', time.localtime())
    # 设置保存文件的名称格式
        filename = filepath + now + 'HTMLtemplate.html'
    # filename = config.report()
        fp = file(filename, 'wb')
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=fp,
           title=u'百度搜索测试报s告',
           description=u'用例执行情况：')
        suit = unittest.TestSuite(tests=(Test_search('test_baidu'))


if __name__ == '__main__':
    run()
    # suit=unittest.TestSuite(tests=(Test_search('test_baidu'))

    # path=os.path.abspath('.')
    # path1=os.path.join(path, "package")
    # filepath=path1 + '/reports/'
    # # 获取系统当前时间
    # now=time.strftime('%Y%m%d%M%H%S', time.localtime())
    # # 设置保存文件的名称格式
    # filename=filepath + now + 'HTMLtemplate.html'
    # # filename = config.report()
    # fp=file(filename, 'wb')
    # runner=HTMLTestRunner.HTMLTestRunner(
    #     stream=fp,
    #     title=u'百度搜索测试报s告',
    #     description=u'用例执行情况：')

    run()
