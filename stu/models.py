import datetime
import django.utils.timezone as timezone
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core import validators
from django.contrib import admin

Project_type = [
    (0, 'photos'),
    (1, 'words'),
    (2, 'others'),
]


class UserInfo2(models.Model):
    objects = models.Manager()
    name = models.CharField(verbose_name="姓名", max_length=16)
    phone = models.CharField(verbose_name="电话", max_length=16)
    CustomerID = models.CharField(verbose_name="身份号码", max_length=16)
    email = models.CharField(verbose_name="邮箱", max_length=32)
    address = models.CharField(verbose_name="地址", max_length=32)
    industry = models.CharField(verbose_name="所属行业", max_length=16)


# Create your models here.


class Project(models.Model):
    # 字段名称
    objects = models.Manager()
    # 项目名称
    project_name = models.CharField(max_length=200, blank=False, verbose_name='project name')
    # 项目作者
    project_author = models.CharField(max_length=200, blank=False, verbose_name='project author')
    # 项目类型
    project_type = models.SmallIntegerField(blank=False, choices=Project_type, verbose_name="project type")
    # 项目不确定性
    # project_uncertainty = models.CharField(max_length=200, blank=False, verbose_name='Measurement uncertainty ')
    # 检测参数
    Test_number = models.CharField(max_length=200, blank=False, verbose_name='Test number')
    # 计量次数
    Metrological = models.CharField(max_length=200, blank=False, verbose_name='Metrological')
    # 技术要求
    TestRequirements = models.CharField(max_length=200, blank=False, verbose_name='TestRequirements')
    # 实测值
    TestValues = models.CharField(max_length=200, blank=False, verbose_name='TestValues')
    # 示值误差
    TestValueError = models.CharField(max_length=200, blank=False, verbose_name='TestValueError')
    # 单项判定
    SingleDetermination = models.CharField(max_length=200, blank=False, verbose_name='SingleDetermination')
    # 项目日期
    # project_data = models.CharField(max_length=200, blank=False, verbose_name='上传日期')
    # # 项目描述
    project_description = models.CharField(max_length=1000, blank=False, verbose_name='Project Description',
                                           default='please enter...')
    # 运行时间
    Upload_time = models.DateTimeField(max_length=100, verbose_name='Upload Time', auto_now=True)
    # 源码
    source_code_url = models.CharField(max_length=100, default='null')

    image = models.ImageField(blank=True, null=True)



class Meta:
    verbose_name = ('ML management')
    # verbose_name = ('机器学习算法管理')
    verbose_name_plural = verbose_name
