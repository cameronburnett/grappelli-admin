# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-07 22:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0029_auto_20170807_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='function',
            name='function',
            field=models.CharField(choices=[('PD', 'PD')], max_length=20),
        ),
        migrations.AlterField(
            model_name='site',
            name='site',
            field=models.CharField(choices=[('SAN', 'San Diego'), ('BLR', 'Bangalore')], max_length=20),
        ),
    ]
