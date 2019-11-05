# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('jixiao', '0004_auto_20191029_0045'),
    ]

    operations = [
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
    ]
