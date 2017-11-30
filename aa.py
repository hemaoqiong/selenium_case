# -*- coding: utf-8 -*-
from selenium import webdriver

driver = webdriver.Firefox()
# driver.get('D:\\py\\AutoTestFramework\\src\\others\\test.html')
driver.get('file:///home/forin/test.html')

# 1.串联寻找
print driver.find_element_by_id('B').find_element_by_tag_name('div').text

# 2.xpath父子关系寻找
print driver.find_element_by_xpath("//div[@id='B']/div").text

# 3.css selector父子关系寻找
print driver.find_element_by_css_selector('div#B>div').text

# 4.css selector nth-child
print driver.find_element_by_css_selector('div#B div:nth-child(1)').text

# 5.css selector nth-of-type
print driver.find_element_by_css_selector('div#B div:nth-of-type(1)').text

# 6.xpath轴 child
print driver.find_element_by_xpath("//div[@id='B']/child::div").text

driver.quit()
