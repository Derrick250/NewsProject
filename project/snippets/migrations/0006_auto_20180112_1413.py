# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-01-12 14:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0005_auto_20180112_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='time',
            field=models.TimeField(default=b'14:13:00'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='time',
            field=models.TimeField(default=b'14:13:00'),
        ),
    ]
