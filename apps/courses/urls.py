# _*_ coding:utf-8 _*_

from django.urls import path,re_path

from .views import CourseView,CourseDetailView,CourseInfoView,CourseCommentsView,AddCommentsView,VideoPlayView


# 要写上APP的名字
app_name ="course"

urlpatterns = [
    path('list/',CourseView.as_view(),name='course_list'),
    # 课程详情
    re_path('detail/(?P<course_id>\d+)/',CourseDetailView.as_view(),name='course_detail'),
    # 章节视频
    re_path('info/(?P<course_id>\d+)/',CourseInfoView.as_view(),name='course_info'),
    # 公开课评论
    re_path('comment/(?P<course_id>\d+)/',CourseCommentsView.as_view(),name='course_comments'),
    # 添加评论
    path('add_comment/',AddCommentsView.as_view(),name='add_comment'),
    # 课程视频播放页
    re_path('video/(?P<video_id>\d+)/', VideoPlayView.as_view(), name="video_play"),

]