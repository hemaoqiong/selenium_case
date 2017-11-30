# coding=utf_8
# import smtplib
# from email.mime.text import MIMEText
# # from email.header import Header

# sender = 'hemao1992@126.com'
# # receive = '2447617382@qq.com'
# receive = 'pieyu1992@163.com'
# # 第三方 SMTP 服务
# smtpserver = 'smtp.126.com'
# username = 'hemao1992@126.com'
# password = 'hemao1992'


# # subject = u'注册与登录 - 注册'    # 邮件主题
# msg = MIMEText(u'为何注册完邮箱后要完善真实信息!', 'plain', 'utf-8')
# # msg['Subject'] = subject
# # msg['To'] = receive
# # msg['From'] = sender

# # smtp = smtplib.SMTP_SSL(smtpserver, 465)
# smtp = smtplib.SMTP(smtpserver, 25)
# smtp.set_debuglevel(1)
# # smtp.connect('smtp.126.com')
# smtp.login(username, password)
# smtp.sendmail(sender, receive, msg.as_string())
# print 'the email has send!'
# smtp.quit()

#######
'''发送失败错误1：smtplib.SMTPAuthenticationError: (550, b'User has no permission')
   我们使用python发送邮件时相当于自定义客户端根据用户名和密码登录，然后使用SMTP服务发送邮件，新注册的163邮箱是默认不开启客户端授权的，因此登录总是被拒绝，解决办法（以163邮箱为例）：进入163邮箱-设置-客户端授权密码-开启（授权码是用于登录第三方邮件客户端的专用密码），非第三方登录密码不变。

错误2：smtplib.SMTPAuthenticationError: (535, b'Error: authentication failed')
　　以163邮箱为例，在开启POP3/SMTP服务，并开启客户端授权密码时会设置授权码，将这个授权码代替smtplib.SMTP().login(user,password)方法中的password即可。
'''


import smtplib
from email.mime.text import MIMEText
mailto_list = ['2447617382<2447617382@qq.com>']  # 收件人(列表)
mail_host = "smtp.126.com"  # 使用的邮箱的smtp服务器地址，这里是163的smtp地址
mail_user = "hemao1992"  # 用户名
mail_pass = "hemao1992"  # 密码
mail_postfix = "126.com"  # 邮箱的后缀，网易就是163.com


def send_mail(to_list, sub, content):
    me = "hemao1992" + "<" + mail_user + "@" + mail_postfix + ">"
    msg = MIMEText(content, _subtype='plain')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)  # 将收件人列表以‘；’分隔
    try:
        server = smtplib.SMTP()
        server.connect(mail_host)  # 连接服务器
        server.set_debuglevel(1)
        server.verify(mailto_list)
        server.login(mail_user, mail_pass)  # 登录操作
        server.sendmail(me, to_list, msg.as_string())
        server.close()
        return True
    except Exception, e:
        print str(e)
        return False


for i in range(1):  # 发送1封，上面的列表是几个人，这个就填几
    if send_mail(mailto_list, "hello.python2", "电话是17828770889"):  # 邮件主题和邮件内容
        # 这是最好写点中文，如果随便写，可能会被网易当做垃圾邮件退信
        print "done!"
    else:
        print "failed!"
