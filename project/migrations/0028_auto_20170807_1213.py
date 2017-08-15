# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-07 19:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0027_auto_20170803_1654'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalproject',
            name='project_function',
        ),
        migrations.RemoveField(
            model_name='historicalproject',
            name='project_site',
        ),
        migrations.RemoveField(
            model_name='project',
            name='project_function',
        ),
        migrations.RemoveField(
            model_name='project',
            name='project_site',
        ),
        migrations.AddField(
            model_name='computeprofile',
            name='function',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='project.Function'),
        ),
        migrations.AddField(
            model_name='function',
            name='site',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='project.Site'),
        ),
        migrations.AddField(
            model_name='historicalcomputeprofile',
            name='function',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='project.Function'),
        ),
        migrations.AddField(
            model_name='historicalstorageprofile',
            name='function',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='project.Function'),
        ),
        migrations.AddField(
            model_name='site',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='project.Project'),
        ),
        migrations.AddField(
            model_name='storageprofile',
            name='function',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='project.Function'),
        ),
    ]
