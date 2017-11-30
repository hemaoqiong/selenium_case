# coding=utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC


# Create a new instance of the Firefox driver
driver = webdriver.Firefox()

# go to the ｂａｉｄｕ home page
driver.get("http://www.baidu.com")

# the page is ajaxy so the title is originally this:
print driver.title

# find the element that's name attribute is kw (the google search box)
inputElement = driver.find_element_by_id("kw")

# type in the search
inputElement.send_keys("cheese!")

# submit the form (although google automatically searches now without
# submitting)
inputElement.submit()

try:
    # we have to wait for the page to refresh, the last thing that seems to be
    # updated is the title
    WebDriverWait(driver, 10).until(EC.title_contains("cheese!"))

    # You should see "cheese!_百度搜索"
    print driver.title

finally:
    driver.quit()

# end
