# coding=utf-8
import time
import os.path
# from selenium import webdriver
# import logging
from log import Logger
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import sys
reload(sys)
sys.setdefaultencoding('utf8')  # 如果不添加以上三行代码，xpath如果表达式包括中文，就会报错，python 2.x 默认
# string 类型是assic类型，在xpath拆分的时候，报codec can't decode byte 0xe4 in position 17: ordinal not in range(128)

now = time.strftime('%Y-%m-%d  %H%M%S', time.localtime())
logger = Logger()


class BasePage(object):
    """
    定义一个页面基类，让所有页面都继承这个类，封装一些常用的页面操作方法到这个类
    """
    """基于原生的selenium框架做了二次封装."""

    def __init__(self, selnium_driver):

        self.driver = selnium_driver

    # 通过title断言进入的页面是否正确。pagetitle为配置的title
    # 使用title获取当前窗口title，检查输入的title是否在当前title中，返回比较结果（True 或 False）

    def on_page(self, pagetitle):
        return pagetitle in self.driver.title
        logger.info("The input pagetitle is %s" % pagetitle,
                    "The  open title is %s" % self.driver.title)

    # open browser
    def open(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    # quit browser and end testing
    def quit(self):
        self.driver.quit()

    # 浏览器前进操作
    def forward(self):
        self.driver.forward()
        logger.info("Click forward on current page.")

    # 浏览器后退操作
    def back(self):
        self.driver.back()
        logger.info("Click back on current page.")

    # 隐式等待
    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)
        logger.info("wait for %d seconds." % seconds)

    # 点击关闭当前窗口
    def close(self):
        try:
            self.driver.close()
            logger.info("Closing and quit the browser.")
        except NameError as e:
            logger.error("Failed to quit the browser with %s" % e)

    # 保存图片

    def scrennshots(self):
        imagepath = os.path.abspath('.')
        imagepath2 = os.path.join(imagepath, 'scrennshots/')
        imagefile = imagepath2 + now + '.png'
        try:
            self.driver.get_screenshot_as_file(imagefile)
            logger.info(
                'Had take screenshot and save to folder : /screenshots')
        except NameError as e:
            logger.error('Failed to take screenshot! %s" % e')
            self.screenshots()

    # 清除文本框
    def clear(self, selector):

        el = self.find_element(selector)
        try:
            el.clear()
            logger.info("Clear text in input box before typing.")
        except NameError as e:
            logger.error("Failed to clear in input box with %s" % e)
            self.get_windows_img()

    # 点击元素
    def click(self, selector):

        el = self.find_element(selector)
        try:
            el.click()
            logger.info("The element \' %s \' was clicked." % el.text)
        except NameError as e:
            logger.error("Failed to click the element with %s" % e)

    # 或者网页标题
    def get_page_title(self):
        logger.info("Current page title is %s" % self.driver.title)
        return self.driver.title

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        logger.info("Sleep for %d seconds" % seconds)

    #   '''定位元素方法封装'''
    def find_element(self, selector, timeout=10):
        '''useage:
        selector = (By.ID,'lbApp')
        driver.find_element(selector)

        '''
        try:
            # element = WebDriverWait(self.driver,10).until(
            #     EC.presence_of_element_located(selector))
            # 先判断元素是否可见，在定位元素
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(selector))
            element = self.driver.find_element(*selector)
            # 这里调用ｌｏｃａｔｏｒ必须加“*”号，不然报错,加星号相当于引用元组里的元素
            # 或者使用匿名函数这个定位元素
         # element = WebDriverWait(self.driver, timeout, 1).until(
         #     lambda x: x.find_element(*selector))
            return element
        except NoSuchElementException as e:
            logger.error("Failed to locate the element.")
            self.scrennshots()

    def send_keys(self, selector, text):
        '''发送文本，清空后输入'''

        # try:
        #     element =self.find_element(selector)
        #     element.clear()
        #     element.send_keys(text)
        # except AttributeError:
        #     # print u"%s 页面中未能找到 %s 元素"%(self, selector)
        #     logger.info(u"%s 页面中未能找到 %s 元素"%(self, selector))
        element = self.find_element(selector)
        element.clear()
        element.send_keys(text)
    # 重写switch_window方法

    def switch_to_window(self):
        '''切换窗口，获取窗口handle'''
        window_name = self.driver.current_window_handle
        self.driver.switch_to.window(window_name)
        print window_name

    # 重写switch_frame方法
    def switch_frame(self, loc):
        return self.driver.switch_to.frame(loc)

    # 定义script方法，用于执行js脚本，范围执行结果
    def script(self, src):
        self.driver.execute_script(src)
