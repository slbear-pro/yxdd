# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banci',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='班次名称', max_length=20)),
                ('index', models.IntegerField(verbose_name='index')),
            ],
            options={
                'verbose_name': '班次',
                'verbose_name_plural': '班次',
                'db_table': 'yx_banci',
            },
        ),
        migrations.CreateModel(
            name='PaiBan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('date', models.DateField(verbose_name='日期')),
                ('userFirst', models.CharField(verbose_name='民警1', max_length=20)),
                ('userSecond', models.CharField(verbose_name='民警2', max_length=20, blank=True, null=True)),
                ('banci', models.ForeignKey(verbose_name='班次', to='zhiban.Banci')),
            ],
            options={
                'verbose_name': '排班表',
                'verbose_name_plural': '排班表',
                'db_table': 'yx_paiban',
            },
        ),
    ]
