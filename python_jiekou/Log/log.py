# coding=utf-8
# import logging


# import os
# import time

# log_pathname = os.path.dirname(os.path.abspath("run_main.py"))
# if not os.path.exists(log_pathname):
#     os.mikdir(log_pathname)


# # time
# time_input = time.strftime(format='% Y % m % d % H % M % S', time.localtime())

# filename = os.path.join(log_pathname, time_input, 'logs')


# def Logger():
#     # 创建一个logger
#     logger = logging.getLogger()
#     logger.setLevel(logging.DEBUG)
#     # 创建一个handler，用于写入日志文件
#     fh = logging.FileHandler(filename, mode='a')
#     fh.setLevel(logging.INFO)
#     # 再创建一个handler，用于输出到控制台
#     ch = logging.StreamHandler()
#     ch.setLevel(logging.WARNING)
#     # 定义handler的输出格式
#     formatter = logging.Formatter(
#         '%(asctime)s-%(filename)s-[line:%(lineno)d]-%(levelname)s:%(message)s')
#     fh.setFormatter(formatter)
#     ch.setFormatter(formatter)
#     # 给logger添加handler
#     logger.addHandler(fh)
#     logger.addHandler(ch)

#     logger.info("dfhgjkdfjsghjkkde")


from selenium import webdriver
# from selenium.webdriver.phantomjs.service import *
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.abstract_event_listener import AbstractEventListener

driver = webdriver.Firefox()
driver.get('http://sahitest.com/demo/label.htm')
# WebDriverWait(driver, timeout, poll_frequency=POLL_FREQUENCY, ignored_exceptions=None)
element1 = driver.find_element_by_id('c1')
AbstractEventListener.before_click(element1, driver)
element1.click()
