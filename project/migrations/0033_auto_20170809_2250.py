# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-10 05:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0032_auto_20170807_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='site',
            field=models.CharField(choices=[('SAN', 'SAN'), ('BLR', 'BLR')], max_length=20),
        ),
    ]