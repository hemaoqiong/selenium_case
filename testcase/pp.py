# coding=utf-8
from selenium import webdriver


class Baidu(object):
    driver = webdriver.Firefox()
    url = 'https://www.baidu.com/s?wd=YOYO&rsv_spt=1&rsv_iqid=0x83399b7c00004797&issp=1&f=8&rsv_bp=0&rsv_idx=2&ie=utf-8&tn=78040160_40_pg&rsv_enter=1&rsv_sug3=6&rsv_sug1=6&rsv_sug7=101&rsv_t=94acM1vOiq%2BxHCrRT2WkRPec5stEe5IPPsCiS4d%2B1Dkjb0T8eJnlc7NDdWN%2BkBnxtEJxWTY&rsv_sug2=0&inputT=3234&rsv_sug4=4008'

    driver.get(url)

    driver.find_element_by_link_text(u'YOYO_百度百科').click()


if __name__ == '__main__':

    bb = Baidu()
