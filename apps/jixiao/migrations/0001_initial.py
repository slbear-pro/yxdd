# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cache',
            fields=[
                ('key', models.CharField(primary_key=True, max_length='20', serialize=False)),
                ('value', models.CharField(max_length='50')),
            ],
            options={
                'db_table': 'yx_cache',
            },
        ),
        migrations.CreateModel(
            name='Jixiao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('process_instance_id', models.CharField(verbose_name='process_instance_id', max_length='50', blank=True)),
                ('time', models.DateField(verbose_name='加分日期')),
                ('comment', models.CharField(verbose_name='加分项目', max_length=200)),
                ('fenzhi', models.DecimalField(verbose_name='分值', max_digits=10, decimal_places=3)),
                ('result', models.CharField(verbose_name='result', max_length=20, blank=True, null=True)),
                ('status', models.CharField(verbose_name='status', max_length=20, blank=True, null=True)),
                ('user', models.ForeignKey(verbose_name='姓名', to='user.User')),
            ],
            options={
                'verbose_name': '绩效',
                'verbose_name_plural': '绩效',
                'db_table': 'yx_jixiao',
            },
        ),
        migrations.CreateModel(
            name='JixiaoTongji',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('year', models.CharField(verbose_name='year', max_length=4, null=True)),
                ('mon', models.CharField(verbose_name='月份', max_length=2, null=True)),
                ('zongfen', models.DecimalField(verbose_name='总分', max_digits=10, decimal_places=3)),
                ('mingci', models.IntegerField(verbose_name='名次', null=True)),
                ('user', models.ForeignKey(verbose_name='姓名', to='user.User')),
            ],
            options={
                'verbose_name': '绩效月报',
                'verbose_name_plural': '绩效月报',
                'db_table': 'yx_jixiaoTongji',
            },
        ),
        migrations.CreateModel(
            name='WrongForm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('instanceid', models.CharField(max_length='50')),
            ],
            options={
                'db_table': 'yx_wrongform',
            },
        ),
    ]
