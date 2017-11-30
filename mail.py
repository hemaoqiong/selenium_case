# coding=utf_8
import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'abc@126.com'
receive = '2447617382@qq.com'
subject = 'pathon send email'

smtpserver = 'smtp.sina.com.cn'
username = 'abc@126.com'
password = '123456'
msg = MIMEText('你好', 'text''utf-8')
msg['subject'] = Header(subject, 'utf-8')
smtp = smtplib.SMTP()
smtp.connect('smtp.126.com')
smtp.login(username, password)
smtp.sendmail(sender, receive, msg.as_string())
smtp.quit()
