# coding=utf-8
# from selenium import webdriver
# from time import sleep
# from BasePage import basepage


# def homepage(self):
#     self.driver = driver
#     self.driver.get(url)
#     sleep(2)
# import requests
# from PIL import Image
# from StringIO import StringIO
# r = requests.get(
#     'http://cn.python-requests.org/zh_CN/latest/_static/requests-sidebar.png')
# i = Image.open(StringIO(r.content))
# i.show()
import requests
headers = {'Connection': 'keep-alive',
           'Content-Length': 385,
           'Accept': 'application/json,text/javascript,*/*;q = 0.01',
           # 'VerificationToken': 'sr2N-GQRoG_CSftWUdmJykCaoBGEsnz-kxXWfKW_GEVKLeQ-avpkeoS43S4T72sDzv1yuxILXeAcpYH2dYrEn5ErNAg1:sI5PzcbzmH3ICwzxYj3bONnf34RVEpANQMpraJYV7frkzobnqI8aUn159B2-07Lpve1T58BICJV-DnDMFCoixTiUELs1',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3064.400 QQBrowser/9.6.11332.400',
           'Content-Type': 'application/json; charset=UTF-8',
           # 'Referer': 'https://passport.cnblogs.com/user/signin?ReturnUrl=http%3A%2F%2Fhome.cnblogs.com%2Fu%2Fhe12345%2F',
           'Accept-Encoding': 'gzip, deflate, br',
           'Accept-Language': 'zh-CN,zh;q=0.8',
           'Cookie': '__gads=ID=78b65628f617f98a:T=1494556849:S=ALNI_MbWOzoT4vtJhp7zIxN6E8gOa7Po4Q;UM_distinctid=15c760d74a1a-092ed9f25dc6ff-31437652-1fa400-15c760d74a2458; _ga=GA1.2.448265553.1493953194; _gid=GA1.2.2010219680.1497233876; SERVERID=227b087667da6f8e99a1165002db93f6|1497337326|1497336069; Hm_lvt_6279c8b8905ad038e867c96dea646c6a=1497336319,1497336438,1497336673,1497337569; Hm_lpvt_6279c8b8905ad038e867c96dea646c6a=1497337569'}
# login
payload = {"input1": "YfNNbAUO3DnFz1I6JJ4gSW1FmLJDr4HhbAKNQ/VpsW1w9Hy5oHN+f0FfA01rD8gN89BO5zx9RhxUOQBE1XjXcjwzzX47j6C6d40HWv2Fuufmmv1UUhBGqdoQsowh646C+EJF6qsXbR87CQV5FPXad49yqmplVdWUuvvYrWxxqYM=",
           "input2": "HQ132YGjAq1og9eGH9dfFV+4bo5jPJjlcBvVjQccWNjzBp3JE+VnDorCYriUMKRANjO75j1sA5WlWbcyH/rJfv20SMlHtozMg6mqc8MOYeah7lBvMT6Or09W1GEL1xETmuGmLpuVrUmmAbPg4iublIb2uewLf+jq9iJLalra9/o=",
           "remember": True}
url = 'https://passport.cnblogs.com/user/signin'
s = requests.Session()
r = s.post(url, json=payload, headers=headers, verify=False)
print r.text
# bao cun cao gao xiang
body = {'__VIEWSTATE': '',
        '__VIEWSTATEGENERATOR': 'FE27D343',
        'Editor$Edit$txbTitle': 'Python自动化测试。',
        'Editor$Edit$EditorBody': 'Python测试hhhhh',
        'Editor$Edit$Advanced$chkDisplayHomePage': 'on',
        'Editor$Edit$Advanced$chkComments': 'on',
        'Editor$Edit$Advanced$chkMainSyndication': 'on',
        'Editor$Edit$lkbDraft': '存为草稿'
        }
url1 = 'https://i.cnblogs.com/EditPosts.aspx?opt=1'
r2 = s.post(url1, body=body, verify=False)
print r2.content
