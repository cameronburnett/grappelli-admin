# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-27 17:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_auto_20170727_1047'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalproject',
            name='compute_profile',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='project.ComputeProfile'),
        ),
        migrations.RemoveField(
            model_name='project',
            name='compute_profile',
        ),
        migrations.AddField(
            model_name='project',
            name='compute_profile',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE,
                                    to='project.ComputeProfile'),
        ),
    ]
