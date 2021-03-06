# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-03 08:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cmdb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ToolsExecDetailHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('exec_result', models.TextField(blank=True, default='', null=True, verbose_name='执行结果')),
                ('err_msg', models.TextField(blank=True, default='', null=True, verbose_name='错误信息')),
                ('host', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cmdb.Host', verbose_name='目标主机')),
            ],
            options={
                'verbose_name': '工具详细信息',
                'verbose_name_plural': '工具详细信息',
            },
        ),
        migrations.CreateModel(
            name='ToolsExecJob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('param', models.TextField(blank=True, default='', null=True, verbose_name='执行参数')),
                ('hosts', models.ManyToManyField(to='cmdb.Host', verbose_name='目标主机')),
            ],
            options={
                'verbose_name': '执行记录',
                'verbose_name_plural': '执行记录',
            },
        ),
        migrations.CreateModel(
            name='ToolsScript',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=255, verbose_name='工具名称')),
                ('tool_script', models.TextField(verbose_name='脚本')),
                ('tool_run_type', models.IntegerField(choices=[(0, 'SaltState'), (1, 'Shell')], default=0, verbose_name='脚本类型')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='工具说明')),
            ],
            options={
                'verbose_name': '工具',
                'verbose_name_plural': '工具',
            },
        ),
        migrations.CreateModel(
            name='ToolsTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=255, verbose_name='类型名称')),
            ],
            options={
                'verbose_name': '工具类型',
                'verbose_name_plural': '工具类型',
            },
        ),
        migrations.AddField(
            model_name='toolsscript',
            name='tools_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tools_manager.ToolsTypes', verbose_name='工具类型'),
        ),
        migrations.AddField(
            model_name='toolsexecjob',
            name='tools',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tools_manager.ToolsScript', verbose_name='工具'),
        ),
        migrations.AddField(
            model_name='toolsexecdetailhistory',
            name='tool_exec_history',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tools_manager.ToolsExecJob'),
        ),
    ]
