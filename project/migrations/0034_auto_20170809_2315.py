# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-10 06:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0033_auto_20170809_2250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalproject',
            name='project_key',
        ),
        migrations.RemoveField(
            model_name='project',
            name='project_key',
        ),
    ]
