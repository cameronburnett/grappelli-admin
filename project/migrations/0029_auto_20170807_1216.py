# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-07 19:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0028_auto_20170807_1213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='computeprofile',
            name='project',
        ),
        migrations.RemoveField(
            model_name='historicalcomputeprofile',
            name='project',
        ),
        migrations.RemoveField(
            model_name='historicalstorageprofile',
            name='project',
        ),
        migrations.RemoveField(
            model_name='storageprofile',
            name='project',
        ),
    ]
