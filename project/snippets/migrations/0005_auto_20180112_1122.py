# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-01-12 11:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0004_auto_20180112_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='time',
            field=models.TimeField(default=b'11:22:13'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='time',
            field=models.TimeField(default=b'11:22:13'),
        ),
    ]
