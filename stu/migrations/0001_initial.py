# Generated by Django 4.1.5 on 2023-01-17 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=200, verbose_name='项目名称')),
                ('project_type', models.SmallIntegerField(choices=[(0, 'app'), (1, 'web'), (2, '其他')], verbose_name='项目类型')),
                ('project_version', models.CharField(max_length=200, verbose_name='项目版本')),
            ],
        ),
    ]
