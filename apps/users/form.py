# _*_ coding:utf-8 _*_

from django import forms
from captcha.fields import CaptchaField

from .models import UserProfile


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True,min_length=5)


class RegisterForm(forms.Form):
    '''注册验证表单'''
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5)
    # 验证码，字段里面可以自定义错误提示信息
    captcha = CaptchaField()


class ForgetpwdForm(forms.Form):
    '''忘记密码'''
    email = forms.EmailField(required=True)
    # 验证码，字段里面可以自定义错误提示信息
    captcha = CaptchaField()


class ModifyPwdForm(forms.Form):
    '''
    重置密码
    '''
    password1 = forms.CharField(required=True, min_length=5)
    password2 = forms.CharField(required=True, min_length=5)


class UploadImageForm(forms.ModelForm):
    '''
    用户更改头像
    '''
    class Meta:
        model = UserProfile
        fields = ['image']


class UserInfoForm(forms.ModelForm):
    '''
    用户资料
    '''
    class Meta:
        model = UserProfile
        fields = ['nick_name', 'birday', 'gender', 'address', 'mobile']