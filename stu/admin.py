from django.contrib import admin

from stu.models import Project

# Register your models here.


# 全局
admin.site.site_header = 'ML management platform'
admin.site.site_title = 'ML management backstage'


# 优化列表
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'project_author', 'project_type', 'project_version', 'project_data')
    list_display = ('id', 'project_name', 'project_author', 'project_type', 'project_uncertainty', 'TestParameters',
                    'Metrological', 'TestRequirements', 'TestValues', 'TestValueError',
                    'SingleDetermination',)
    # list_display = ('id', 'project_name', 'project_author', 'project_type', 'project_uncertainty',)

    list_display_links = ('id', 'project_name')  # 设置字段链接

    list_filter = ['project_name', 'project_type', 'project_author']

    list_per_page = 5
    actions_on_top = False
    search_fields = ('project_name',)
    # readonly_fields = ('project_name', 'project_author', 'project_type', 'project_uncertainty',)  # 无法修改

admin.site.register(Project, ProjectAdmin)
