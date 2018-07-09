# _*_ coding:utf-8 _*_

from django.urls import path,re_path

from .views import UserInfoView,UploadImageView,UpdatePwdView,SendEmailCodeView,UpdateEmailView,MyCourseView,MyFavOrgVie,MyFavTeacherView,MyFavCourseView,MyMessageView,LogOutView

# 要写上APP的名字
app_name ="users"

urlpatterns = [
    # 个人中心
    path('info/', UserInfoView.as_view(), name='user_info'),

    # 用户头像上传
    path('image/upload/', UploadImageView.as_view(), name='image_upload'),

    # 用户修改密码
    path('update/pwd/', UpdatePwdView.as_view(), name='pudate_pwd'),

    # 发送邮箱验证码
    path('sendemail_code/', SendEmailCodeView.as_view(), name='sendemail_code'),

    # 修改邮箱
    path('update_email/', UpdateEmailView.as_view(), name='update_email'),

    # 我的课程
    path('mycourse/', MyCourseView.as_view(), name='mycourse'),

    # 我的收藏的课程机构
    path('myfav/org/', MyFavOrgVie.as_view(), name='myfav_org'),

    # 我的收藏的授课教师
    path('myfav/teacher/', MyFavTeacherView.as_view(), name='myfav_teacher'),

    # 我的收藏的公开课程
    path('myfav/course/', MyFavCourseView.as_view(), name='myfav_course'),

    # 我的消息
    path('my_message/', MyMessageView.as_view(), name='my_message'),

    # 用户登出
    path('logout/', LogOutView.as_view(), name='logout')
]