# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-01-15 14:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0006_auto_20180112_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='date',
            field=models.DateField(default=b'2018-01-15'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='time',
            field=models.TimeField(default=b'14:09:49'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='date',
            field=models.DateField(default=b'2018-01-15'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='time',
            field=models.TimeField(default=b'14:09:49'),
        ),
    ]