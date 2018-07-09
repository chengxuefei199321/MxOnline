# _*_ encoding:utf-8 _*_
from datetime import datetime

from django.db import models



# Create your models here.


class CityDict(models.Model):
    name = models.CharField(max_length=50,verbose_name=u"城市")
    desc = models.CharField(max_length=200,verbose_name=u"描述")
    add_time = models.DateTimeField(datetime.now)

    class Meta:
        verbose_name = u"城市"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseOrg(models.Model):
    '''
    课程机构
    '''

    name = models.CharField(max_length=50,verbose_name=u"机构名称")
    desc = models.TextField(verbose_name=u"机构描述")
    ORG_CHOICES = (("pxjg",u"培训机构"),("gr",u"个人"),("gx",u"高校"))
    category = models.CharField(max_length=20,choices=ORG_CHOICES,verbose_name=u"机构类别",default="pxjg")
    tag = models.CharField(max_length=10, default=u"程氏集团", verbose_name=u"机构标签")
    click_nums = models.IntegerField(default=0,verbose_name=u"点击数")
    fav_nums = models.IntegerField(default=0,verbose_name=u"收藏数")
    image = models.ImageField(upload_to="org/%Y/%m",max_length=100,verbose_name=u"logo")
    address = models.CharField(max_length=150,verbose_name=u"机构地址")
    city = models.ForeignKey(CityDict,on_delete=models.CASCADE,verbose_name=u"所在城市")
    students = models.IntegerField(default=0,verbose_name=u"学习人数")
    course_nums = models.IntegerField(default=0,verbose_name=u"课程数")
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"课程机构"
        verbose_name_plural = verbose_name

    #统计教师数量
    def get_teacher_nums(self):
        return  self.teacher_set.all().count()

    def get_course_nums(self):
        #获取课程数
        return self.course_set.all().count()

    def __str__(self):
        return self.name


class Teacher(models.Model):
    org = models.ForeignKey(CourseOrg,on_delete=models.CASCADE,verbose_name=u"所属机构")
    name = models.CharField(max_length=50,verbose_name=u"教师名")
    work_years = models.IntegerField(default=0,verbose_name=u"工作年限")
    work_company = models.CharField(max_length=50,verbose_name=u"就职公司")
    work_position = models.CharField(max_length=50,verbose_name=u"公司职位")
    age = models.IntegerField(default=25,verbose_name=u"年龄")
    points = models.CharField(max_length=50,verbose_name=u"教学特点")
    click_nums = models.IntegerField(default=0,verbose_name=u"点击数")
    fav_nums = models.IntegerField(default=0,verbose_name=u"收藏数")
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u"收藏时间")
    image = models.ImageField(default='',upload_to="teacher/%Y/%m",verbose_name=u"头像",max_length=100)

    class Meta:
        verbose_name = u"教师"
        verbose_name_plural = verbose_name

    # 获取课程数
    def get_course_nums(self):
        return self.course_set.all().count()

    # 获取课程
    # def get_course(self,teacher):
    #     return self.course_set.filter(name=teacher.name)

    def __str__(self):
        return self.name
