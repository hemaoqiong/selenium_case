# coding=utf-8

from selenium import webdriver
# from page_objects import PageElement,PageObject
# class Page(PageObject):
#     star_5=PageElement(xpath='/html/body/div[1]/form/div[3]/div/div[1]/div[1]/div/div[2]/div/div/i[5]')
#     check_box=PageElement(xpath='//@class="check_box")
#         /html/body/div[1]/form/div[3]/div/div[1]/div[2]/div/div[2]/div/label[4]/div[2]

driver = webdriver.Firefox()
driver.get("https://jinshuju.net/f/kRXoEv")
m = driver.find_element_by_xpath("//i[5]")
m.click()
s = driver.find_element_by_xpath(
    '//label[4]/div[2]')
s.click()
driver.find_element_by_tag_name("textarea").send_keys("hbsjdfgjbfdjsjk")
driver.find_element_by_xpath(
    "//input[@id='entry_field_4']").send_keys("2447617389@qq.com")
driver.find_element_by_name("commit").click()
driver.quit()
