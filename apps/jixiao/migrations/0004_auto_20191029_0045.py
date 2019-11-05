# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jixiao', '0003_jixiaotongji'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jixiaotongji',
            name='user',
        ),
        migrations.DeleteModel(
            name='JixiaoTongji',
        ),
    ]
