# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time
# driver = webdriver.Firefox()
driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
driver.implicitly_wait(20)
m = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[3]/a[8]')
time.sleep(2)
ActionChains(driver).move_to_element(m).perform()
# driver.find_element_by_xpath("/html/body/div[2]/div[6]/a[1]").click()
driver.find_element_by_link_text('搜索设置').click()
t = driver.find_element_by_id('nr')
Select(t).select_by_index(0)
