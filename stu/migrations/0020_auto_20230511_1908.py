# Generated by Django 3.2 on 2023-05-11 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=200, verbose_name='project name')),
                ('project_author', models.CharField(max_length=200, verbose_name='project author')),
                ('project_type', models.SmallIntegerField(choices=[(0, 'photos'), (1, 'words'), (2, 'others')],
                                                          verbose_name='project type')),
                ('Test_number', models.CharField(max_length=200, verbose_name='Test number')),
                ('Metrological', models.CharField(max_length=200, verbose_name='Metrological')),
                ('TestRequirements', models.CharField(max_length=200, verbose_name='TestRequirements')),
                ('TestValues', models.CharField(max_length=200, verbose_name='TestValues')),
                ('TestValueError', models.CharField(max_length=200, verbose_name='TestValueError')),
                ('SingleDetermination', models.CharField(max_length=200, verbose_name='SingleDetermination')),
                ('project_description',
                 models.CharField(default='please enter...', max_length=1000, verbose_name='Project Description')),
                ('Upload_time', models.DateTimeField(auto_now=True, max_length=100, verbose_name='Upload Time')),
                ('source_code_url', models.CharField(default='null', max_length=100)),
                ('image', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ), ]

