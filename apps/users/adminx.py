# _*_ coding:utf-8 _*_

import xadmin
from xadmin import views

from .models import EmailVerifyRecord,Banner


class BaseSetting(object):
    # 要使用xadmin的主题功能
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "程雪飞后台管理系统"
    site_footer = "程雪飞在线网"
    # 左侧栏的显示样式
    menu_style = "accordion"


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code','email','send_type']
    list_filter = ['code','email','send_type','send_time']
    model_icon = 'fa fa-address-book-o'


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index','add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index','add_time']


xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)
xadmin.site.register(Banner,BannerAdmin)
xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSettings)

