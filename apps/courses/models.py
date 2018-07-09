# _*_ encoding:utf-8 _*_
from datetime import datetime

from DjangoUeditor.models import UEditorField
from django.db import models

from organization.models import CourseOrg,Teacher


# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"课程名")
    desc = models.CharField(max_length=300, verbose_name=u"课程描述")
    detail =UEditorField(width=600, height=300, toolbars="full", imagePath="courses/ueditor/", filePath="courses/ueditor/", verbose_name=u"课程详情")
    teacher = models.ForeignKey(Teacher, verbose_name='讲师', null=True, blank=True, on_delete=models.CASCADE)
    youneed_know = models.CharField('课程须知', max_length=300, default='')
    teacher_tell = models.CharField('老师告诉你', max_length=300, default='')
    degree = models.CharField(max_length=2, choices=(("cf", "初级"), ("zj", "中级"), ("gj", "高级")),verbose_name=u"难度")
    learn_times = models.IntegerField(default=0, verbose_name=u"学习时长（分钟数）")
    is_banner = models.BooleanField(default=False, verbose_name=u"是否是轮播图的课程")
    students = models.IntegerField(default=0, verbose_name=u"学习人数")
    fav_nums = models.IntegerField(default=0, verbose_name=u"收藏人数")
    image = models.ImageField(max_length=100, upload_to="courses/%Y/%m", verbose_name=u"封面图")
    click_nums = models.IntegerField(default=0, verbose_name=u"点击数")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    course_org = models.ForeignKey(CourseOrg,on_delete=models.CASCADE,verbose_name=u"所属机构",null=True,blank=True)
    category = models.CharField(default='',max_length=20,verbose_name=u"课程类别",null=True,blank=True)
    tag = models.CharField(default='',max_length=10,verbose_name=u"课程标签")


    class Meta:
        verbose_name = u"课程"
        verbose_name_plural = verbose_name

    def get_zj_nums(self):
        # 获取课程的章节数
        return self.lesson_set.all().count()

    # 在后台显示的名称
    get_zj_nums.short_description = u"章节数"


    def get_course_lesson(self):
        # 获取章节
        return self.lesson_set.all()

    def get_learn_users(self):
        #获取这门课程的学习用户
        return self.usercourse_set.all()

    def __str__(self):
        return self.name

    def go_to(self):
        from django.utils.safestring import mark_safe
        # mark_safe后就不会转义
        return mark_safe("<a href='https://home.cnblogs.com/u/derek1184405959/'>跳转</a>")
    go_to.short_description = "跳转"


class BannerCourse(Course):
    class Meta:
        verbose_name = u"轮播课程"
        verbose_name_plural = verbose_name
        # 这里必须设置proxy=True，这样就不会再生成一张表，同时还具有Model的功能
        proxy = True

class Lesson(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE,verbose_name=u"课程")
    name = models.CharField(max_length=100, verbose_name=u"章节名")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"章节"
        verbose_name_plural = verbose_name

    def get_lesson_vedio(self):
        # 获取章节视频
        return self.video_set.all()

    def __str__(self):
        return self.name




class Video(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE,verbose_name=u"章节")
    name = models.CharField(max_length=100, verbose_name=u"视频名")
    url = models.CharField(max_length=200, default='', verbose_name=u"访问地址")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    learn_times = models.IntegerField(default=0, verbose_name=u"学习时长（分钟数）")

    class Meta:
        verbose_name = u"视频"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseResource(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE,verbose_name=u"课程")
    name = models.CharField(max_length=100, verbose_name=u"名称")
    download = models.FileField(max_length=100, upload_to="course/resource/%Y/%m", verbose_name=u"资源文件")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"课程资源"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
