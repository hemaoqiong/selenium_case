# coding=utf-8
from selenium import webdriver
from page_objects import PageElement, PageObject


class SeverPage(PageObject):
    star = PageElement(xpath='//i[5]')
    check_box = PageElement(xpath='//label[4]/div[2]')
    text1 = PageElement(tag_name='textarea')
    input1 = PageElement(xpath="//input[@id='entry_field_4']")
    elm_button = PageElement(name='commit')

    driver = webdriver.PhantomJS()
    driver.root_url = 'https://jinshuju.net/f/kRXoEv'
    page = SeverPage(driver)
    page.get('/')
    page.star.click()  # choose 5 star
    page.check_box.click()  # choose 各种公开课
    page.text1.send_keys('good!')   # write different opion
    page.input1.send_keys('2447617389@qq.com')   #write email number
    page.elm_button.click()  # click submmit button
