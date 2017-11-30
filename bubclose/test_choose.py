# coding = utf - 8
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# import sys
import os

driver = webdriver.Firefox()
# driver = webdriver.Firefox()
driver.get('http://yysl.sz3e.com/wsyysq/select_sldw_zbs.jsp')
time.sleep(2)
# all_data = driver.find_elements_by_xpath('//label@[class="current"]')
all_data = driver.find_elements(By.XPATH, "//label[@class='current']")
data = [data.text for data in all_data]
filepath = os.path.dirname(os.path.abspath('.') + '/scrennshots/')
tim = time.strftime('%Y%m%d %H:%M', time.localtime())
filename = filepath + tim + 'png'
driver.get_screenshot_as_file(filename)
# ddriver.get_screenshot_as_base64


driver = webdriver.Firefox()
driver.get('http://www.baidu.com')
i=driver.find_elements_by_id('kw')
i.clear()
i.send_keys(u'何茂琼')
