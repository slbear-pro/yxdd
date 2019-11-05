# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(verbose_name='userid', primary_key=True, max_length=20, unique=True, serialize=False)),
                ('name', models.CharField(verbose_name='姓名', max_length=20)),
                ('bumen', models.SmallIntegerField(verbose_name='部门', default=0, choices=[(0, '大队部'), (1, '驻外')])),
                ('jiaose', models.CharField(verbose_name='角色', max_length=50, blank=True, null=True)),
            ],
            options={
                'verbose_name': 'minjing',
                'verbose_name_plural': 'minjing',
                'db_table': 'yx_user',
            },
        ),
    ]
