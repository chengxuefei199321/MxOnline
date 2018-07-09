# _*_ coding:utf-8 _*_

from random import Random
from django.core.mail import send_mail

from users.models import EmailVerifyRecord
from MxOnline.settings import EMAIL_HOST_FROM


# 生成随机字符串
def random_str(random_length = 8):
    str = ''
    #生成字符串的可选字符串
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(random_length):
        str += chars[random.randint(0,length)]
    return str


# 发送注册邮件
def send_register_email(email, send_type="register"):
    # 发送之前先保存到数据库，到时候查询链接是否存在
    # 实例化一个EmailVerifyRecord对象
    email_recode = EmailVerifyRecord()
    # 生成随机的CODE放入连接
    if send_type == 'update_email':
        code = random_str(4)
    else:
        code = random_str(16)
    email_recode.code = code
    email_recode.email = email
    email_recode.send_type = send_type

    email_recode.save()

    # 定义邮件内容
    email_title = ""
    email_body = ""

    if send_type == "register":
        email_title = "NBA注册激活连接"
        email_body = "请点击下面的连接激活你的账号：http://127.0.0.1:8000/active/{0}".format(code)

    # 使用Django内置函数完成邮件发送。四个参数：主题，邮件内容，发件人邮箱地址，收件人（是一个字符串列表）
        send_status = send_mail(email_title,email_body,EMAIL_HOST_FROM,[email])
    # 如果发送成功
        if send_status:
            pass
    elif send_type == "forget":
        email_title = "NBA密码重置连接"
        email_body = "请点击下面的连接重置密码：http://127.0.0.1:8000/reset/{0}".format(code)

        # 使用Django内置函数完成邮件发送。四个参数：主题，邮件内容，发件人邮箱地址，收件人（是一个字符串列表）
        send_status = send_mail(email_title, email_body, EMAIL_HOST_FROM, [email])
    # 如果发送成功
        if send_status:
            pass

    elif send_type == "update_email":
        email_title = "NBA邮箱修改验证码连接"
        email_body = "请点击下面的连接重置密码：{0}".format(code)

        # 使用Django内置函数完成邮件发送。四个参数：主题，邮件内容，发件人邮箱地址，收件人（是一个字符串列表）
        send_status = send_mail(email_title, email_body, EMAIL_HOST_FROM, [email])
        # 如果发送成功
        if send_status:
            pass
