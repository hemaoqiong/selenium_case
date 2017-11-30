# coding=utf-8
from selenium import webdriver
driver = webdriver.Firefox()
driver.get('file:///home/forin/test3.html')
# 1.xpath: `.`代表当前节点; '..'代表父节点

# print driver.find_element_by_xpath("// div[@id='C'] / ..").text
# print driver.find_element_by_xpath("//div[@id='D']/..").text
print driver.find_element_by_xpath("//div[@id='D']/../div[3]").text

driver.quit()
