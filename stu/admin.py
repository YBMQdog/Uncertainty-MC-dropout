from django.contrib import admin
from django.utils.html import format_html

from stu.models import Project
from django import forms
# 全局设置
admin.site.site_header = 'ML management platform'
admin.site.site_title = 'ML management backstage'
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        widgets = {
            'TestRequirements': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            "project_description": forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }

# 优化列表
class ProjectAdmin(admin.ModelAdmin):
    form = ProjectForm
    # 列表显示的字段
    list_display = ('id', 'project_name', 'project_author', 'project_type', 'Test_number',
                    'Metrological', 'TestRequirements', 'TestValues', 'TestValueError',
                    'SingleDetermination', 'link')
    fields = ["project_name", "project_author", "project_type", "Test_number", "Metrological",
              "TestValues", "TestValueError", "SingleDetermination","source_code_url", "project_description",
              "TestRequirements",]

  
    # 设置字段链接
    list_display_links = ('id', 'project_name')

    # 过滤器
    list_filter = ['project_name', 'project_type', 'project_author']

    # 每页显示的记录数
    list_per_page = 5

    # 是否在顶部显示操作选项
    actions_on_top = False

    # 搜索字段
    search_fields = ('project_name',)

    # 只读字段（无法修改）
    # readonly_fields = ('project_name', 'project_author', 'project_type', 'project_uncertainty',)

    # 自定义方法，用于在列表中显示超链接
    def link(self, obj):
        url = "http://127.0.0.1:8000/user_detail/"  # 跳转的超链接
        url_text = "contact"  # 显示的文本
        return format_html('<a href="{}" target="_blank">{}</a>'.format(url, url_text))

    link.allow_tags = True
    link.short_description = ""


# 注册模型和模型管理类
admin.site.register(Project, ProjectAdmin)
