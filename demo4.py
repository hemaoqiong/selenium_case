# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.keys import Keys

# driver = webdriver.Firefox()
# driver.get("http://www.python.org")
# driver.implicitly_wait(30)
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page(_source
# driver.close()

# import unittest
# import requests


# class StaticServerTest(unittest.TestCase):

#     def setUp(self):
#         pass

#     def tearDown(self):
#         pass

#     def test_jquery_js_release(self):
#         test_js_url = 'https://code.jquery.com/jquery-2.1.4.min.js'
#         res = requests.get(test_js_url)
#         self.assertEqual(200, res.status_code, msg='jianchashifzhwngcfanh')

# #     def test_http_static_allow_origin(self):
# #         test_js_url = 'https://code.jquery.com/jquery-2.1.4.min.js'
# #         res = requests.get(test_js_url)
"""
requrst
"""

# import requests
# payload = {'key1': 'value1', 'key2': 'value2'}
# r = requests.get('http://httpbin.org/get', params=payload)
# print r.url
# print r.text
# #


# response headers

# import requests
# r = requests.get('http://www.baidu.com', params=None)
# print r.headers
# print r.headers['Content-Type']   #1
# print r.headers.get('Content-Type')  #2

# cookies
# import requests
# url = 'http://www.baidu.com'
# r = requests.get(url, params=None)
# a = r.cookies
# print a

# or  11111
# import requests
# url = 'http://httpbin.org/cookies'
# cookies = dict(cookies_are='working')
# r = requests.get(url, cookies=cookies)

# print r.text

# {
#   "cookies": {
#     "cookies_are": "working"
#   }
# }

