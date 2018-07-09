# _*_ coding:utf-8 _*_

import xadmin

from .models import Course,Lesson,Video,CourseResource,BannerCourse


class LessonInline(object):
    model = Lesson
    extra = 0


class CourseResourceInline(object):
    model = CourseResource
    extra = 0


class CourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times','students','fav_nums','image','click_nums','add_time','add_time','get_zj_nums','go_to']
    search_fields = ['name', 'desc', 'detail', 'degree', 'learn_times','students','fav_nums','image','click_nums','add_time']
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times','students','fav_nums','image','click_nums','add_time','add_time']
    # 图标
    model_icon = 'fa fa-book'
    # 排序
    ordering =['-click_nums']
    # 只读字段，不能编辑
    readonly_fields = ['click_nums']
    # 不显示的字段
    exclude = ['fav_nums']
    # 在列表页面可以直接编辑
    list_editable = ['desc', 'degree']
    # 定时刷新，单位是秒
    refresh_times = [3,5]
    # detail就是要显示为富文本的字段名
    style_fields = {"detail":"ueditor"}

    # 在CourseAdmin中使用inlines添加上面两个的方法
    # 增加章节和课程资源
    inlines = [LessonInline, CourseResourceInline]

    def queryset(self):
        # 重载queryset方法来过滤我们想要的数据
        qs = super(CourseAdmin, self).queryset()
        # 只显示is_banner=False的数据
        qs = qs.filter(is_banner=False)
        return qs

    def save_models(self):
        # 在保存课程的时候统计课程机构的课程数
        # obj实际是一个course对象
        obj = self.new_obj
        # 如果这里不保存，新增课程，统计的课程数会少一个
        obj.save()
        # 确定课程的课程机构存在
        if obj.course_org is not None:
            # 找到添加的课程的课程机构
            course_org = obj.course_org
            # 课程机构的课程数量等于添加课程后的数量
            course_org.course_nums = Course.objects.filter(course_org=course_org).count()
            course_org.save()


class BannerCourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times','students','fav_nums','image','click_nums','add_time','add_time']
    search_fields = ['name', 'desc', 'detail', 'degree', 'learn_times','students','fav_nums','image','click_nums','add_time']
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times','students','fav_nums','image','click_nums','add_time','add_time']
    # 图标
    model_icon = 'fa fa-book'
    # 排序
    ordering =['-click_nums']
    # 只读字段，不能编辑
    readonly_fields = ['click_nums']
    # 不显示的字段
    exclude = ['fav_nums']
    # 增加章节和课程资源
    inlines = [LessonInline, CourseResourceInline]


    def queryset(self):
        # 重载queryset方法来过滤我们想要的数据
        qs = super(BannerCourseAdmin, self).queryset()
        # 只显示is_banner=True的数据
        qs = qs.filter(is_banner=True)
        return qs


class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    list_filter = ['course__name', 'name', 'add_time']


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'name', 'add_time']


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download', 'add_time']
    search_fields = ['course', 'name', 'download']
    list_filter = ['course__name', 'name', 'download', 'add_time']

# 将管理器与model进行注册关联
xadmin.site.register(Course,CourseAdmin)
xadmin.site.register(BannerCourse,BannerCourseAdmin)
xadmin.site.register(Lesson,LessonAdmin)
xadmin.site.register(Video,VideoAdmin)
xadmin.site.register(CourseResource,CourseResourceAdmin)