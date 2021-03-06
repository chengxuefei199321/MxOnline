# _*_ coding:utf-8 _*_

from organization.views import OrgView,AddUserAskView,OrgHomeView,OrgCourseView,OrgDescView,OrgTeacherView,AddFavView,TeacherListView,TeacherDetailView
from django.urls import path,re_path


# 要写上APP的名字
app_name ="organization"

urlpatterns = [
    path('list/',OrgView.as_view(),name='org_list'),
    path('add_ask/',AddUserAskView.as_view(),name='add_ask'),
    re_path('home/(?P<org_id>\d+)/',OrgHomeView.as_view(),name='org_home'),
    re_path('course/(?P<org_id>\d+)/',OrgCourseView.as_view(),name='org_course'),
    re_path('desc/(?P<org_id>\d+)/',OrgDescView.as_view(),name='org_desc'),
    re_path('org_teacher/(?P<org_id>\d+)/',OrgTeacherView.as_view(),name='org_teacher'),

    # 用户收藏
    path('add_fav/',AddFavView.as_view(),name='add_fav'),

    # 授课教师
    path('teacher/list/',TeacherListView.as_view(),name='teacher_list'),

    # 授课教师详情
    re_path('teacher/detail/(?P<teacher_id>\d+)/', TeacherDetailView.as_view(), name="teacher_detail"),
]
