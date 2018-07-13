# _*_ coding:utf-8 _*_

import re

from django import forms

from operation.models import UserAsk

class UserAskForm(forms.ModelForm):
    '''我要咨询'''
    class Meta:
        model = UserAsk
        fields = ['name','mobile','course_name']

    '''调用UserAskForm时会自动调用下面这个方法，下面这个方法必须这样命名'''
    def clean_mobile(self):
        """
        验证手机号码是否合法
        """
        mobile = self.cleaned_data['mobile']
        REGEX_MOBILE = "^1[358]\d{9}$|^147\d{8}$|176\d{8}$"
        p = re.compile(REGEX_MOBILE)
        if p.match(mobile):
            return mobile
        else:
            # 如果手机号不合法
            raise forms.ValidationError(u"手机号码非法",code="mobile_invalid")