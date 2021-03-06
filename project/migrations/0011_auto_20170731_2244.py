# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-01 05:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0010_auto_20170728_1133'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalproject',
            name='compute_profile',
        ),
        migrations.RemoveField(
            model_name='historicalproject',
            name='storage_profile',
        ),
        migrations.RemoveField(
            model_name='project',
            name='compute_profile',
        ),
        migrations.RemoveField(
            model_name='project',
            name='storage_profile',
        ),
        migrations.AddField(
            model_name='computeprofile',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project.Project'),
        ),
        migrations.AddField(
            model_name='historicalcomputeprofile',
            name='project',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='project.Project'),
        ),
        migrations.AddField(
            model_name='historicalstorageprofile',
            name='project',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='project.Project'),
        ),
        migrations.AddField(
            model_name='storageprofile',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project.Project'),
        ),
    ]
