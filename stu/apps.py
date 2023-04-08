from django.apps import AppConfig
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
class StuConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'stu'
    verbose_name="小叶的测试平台"

