# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-21 06:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='user_type',
            field=models.IntegerField(choices=[(1, '普通用户'), (2, 'vip'), (3, 'svip')], default=1),
            preserve_default=False,
        ),
    ]
