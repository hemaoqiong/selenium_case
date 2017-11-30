# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time


class Wangyi():
    def __init__(self):
        self.driver = webdriver.Firefox()

    def open(self, url):
        # url='http://www.163.com/'
        self.driver.get(url)
    def get_title(self):
        print self.driver.title

    def click_new(self):
        loc = u'网易首页'
        self.driver.find_element_by_link_text(loc).click()
    # click ad

    def click(self):
        loc = (By.ID, 'theme')
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(loc))
        element.click()

    def scrennshots(self):
        imagepath = os.path.abspath('.')
        print 'imagepath is %s' % imagepath

        imagepath2 = os.path.join(imagepath, 'scrennshots/')
        print 'imagepath2 is %s' % imagepath2
        now = time.strftime('%Y-%m-%d  %H%M%S', time.localtime())
        imagefile = imagepath2 + now + '.png'
        self.driver.get_screenshot_as_file(imagefile)


# driver = webdriver.Firefox()
# driver.get('http://www.baidu.com')
# i = driver.find_element_by_id('kw')
# i.clear()
# i.send_keys(u'何茂琼')
# imagepath = os.path.abspath('.')
# print 'imagepath is %s' % imagepath

# imagepath2 = os.path.join(imagepath, 'scrennshots/')
# print 'imagepath2 is %s' % imagepath2
# now = time.strftime('%Y-%m-%d  %H%M%S', time.localtime())
# imagefile = imagepath2 + now + '.png'
# # driver.get_screenshot_as_file(imagefile)

# driver.save_screenshot(imagefile)
# driver.quit()
