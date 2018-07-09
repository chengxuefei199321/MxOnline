# _*_ encoding:utf-8 _*_
"""MxOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
import xadmin
from django.views.static import serve

from django.views.generic import TemplateView

from users.views import LoginView,RegisterView,ActiveUserView,ForgetPwdView,ResetView,ModifyPwdView,IndexView

from MxOnline.settings import MEDIA_ROOT


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('xadmin/',xadmin.site.urls),
    path('',IndexView.as_view(),name="index"),
    path('login/',LoginView.as_view(),name="login"),
    path('register/', RegisterView.as_view(), name="register"),
    path("captcha/", include('captcha.urls')),
    re_path('active/(?P<active_code>.*)/',ActiveUserView.as_view(),name="user_active"),
    path('forget/',ForgetPwdView.as_view(),name="forget_pwd"),
    re_path('reset/(?P<active_code>.*)/', ResetView.as_view(), name="reset_pwd"),
    path('modify_pwd/', ModifyPwdView.as_view(), name="modify_pwd"),

    # 课程机构首页url
    path("org/", include('organization.urls', namespace="org")),

    # 课程相关首页url
    path("course/", include('courses.urls', namespace="course")),

    # 处理图片显示的url,使用Django自带serve,传入参数告诉它去哪个路径找，我们有配置好的路径MEDIAROOT
    re_path(r'^media/(?P<path>.*)',serve,{"document_root":MEDIA_ROOT}),


    # re_path(r'^static/(?P<path>.*)',serve,{"document_root":STATIC_ROOT}),

    # 用户相关url
    path("users/", include('users.urls', namespace="users")),

    # UEDITOR编辑器插件
    path('ueditor/',include('DjangoUeditor.urls')),
]

# 全局404配置页面
handler404 = 'users.views.page_not_found'
# 全局500配置页面
handler500 = 'users.views.page_error'
