# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-02-08 14:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0010_auto_20180116_0758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='date',
            field=models.DateField(default=b'2018-02-08'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='time',
            field=models.TimeField(default=b'14:04:01'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='date',
            field=models.DateField(default=b'2018-02-08'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='time',
            field=models.TimeField(default=b'14:04:01'),
        ),
    ]
