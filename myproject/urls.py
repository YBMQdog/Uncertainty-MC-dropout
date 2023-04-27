"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from stu import views
from stu.view import upload
from stu.view import run
from django.conf.urls.static import static
from django.conf import  settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('project/', include('stu.urls')),
    path('test/', views.test),
    path('run/',run.run),
    path('post/', upload.upload_list),  # 上传文件
    path('user_detail/', views.user_detail),
    path('add', views.add_client),
    path('change_form/add', views.add_client),
    path('change_form/change_form/add', views.add_client),


]


