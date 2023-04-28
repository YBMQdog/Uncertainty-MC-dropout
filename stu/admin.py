from django.contrib import admin
from django.utils.html import format_html

from stu.models import Project

# Register your models here.


# 全局
admin.site.site_header = 'ML management platform'
admin.site.site_title = 'ML management backstage'


# 优化列表
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'project_author', 'project_type', 'project_uncertainty', 'TestParameters',
                    'Metrological', 'TestRequirements', 'TestValues', 'TestValueError',
                    'SingleDetermination', 'link')
    # list_display = ('id', 'project_name', 'project_author', 'project_type', 'project_uncertainty',)

    list_display_links = ('id', 'project_name')  # 设置字段链接


    list_display_links = ('project_name','link')
    list_filter = ['project_name', 'project_type', 'project_author']

    list_per_page = 5
    actions_on_top = False
    search_fields = ('project_name',)
    # readonly_fields = ('project_name', 'project_author', 'project_type', 'project_uncertainty',)  # 无法修改


    def link(self, obj):
        url = "http://127.0.0.1:8000/user_detail/"  # 跳转的超链接
        url_text = "contact "  # 显示的文本
        return format_html(u'<a href="{}" target="_blank">{}</a>'.format(url, url_text))
    link.allow_tags = True
    link.short_description = ""


admin.site.register(Project, ProjectAdmin)
