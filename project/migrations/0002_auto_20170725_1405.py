# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-25 21:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalproject',
            name='project_version',
            field=models.CharField(choices=[('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7), ('8', 8), ('9', 9)], max_length=2, verbose_name='Version'),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_version',
            field=models.CharField(choices=[('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7), ('8', 8), ('9', 9)], max_length=2, verbose_name='Version'),
        ),
    ]
