from django.db import models

Project_type = [
    (0, 'photos'),
    (1, 'words'),
    (2, 'others'),
]


# Create your models here.
class Project(models.Model):
    # 字段名称

    # 项目名称
    project_name = models.CharField(max_length=200, blank=False, verbose_name='project name')
    # 项目作者
    project_author = models.CharField(max_length=200, blank=False, verbose_name='project author')
    # 项目类型
    project_type = models.SmallIntegerField(blank=False, choices=Project_type, verbose_name="project type")
    # 项目不确定性
    project_uncertainty = models.CharField(max_length=200, blank=False, verbose_name='Measurement uncertainty ')
    # 检测参数
    TestParameters = models.CharField(max_length=200, blank=False, verbose_name='TestParameters')
    # 计量特性
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
    run_time = models.CharField(max_length=100, default='2023-03-13 13:43:38')
    # 源码
    source_code_url = models.CharField(max_length=100, default='null')
    # 训练集
    train_set_url = models.CharField(max_length=100, default='null')
    # 测试集
    test_set_url = models.CharField(max_length=100, default='null')


    class Meta:
        verbose_name = ('ML management')
        # verbose_name = ('机器学习算法管理')
        verbose_name_plural = verbose_name

