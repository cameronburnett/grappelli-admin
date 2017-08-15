# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-27 18:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0007_auto_20170727_1054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalproject',
            name='compute_apr',
        ),
        migrations.RemoveField(
            model_name='historicalproject',
            name='compute_aug',
        ),
        migrations.RemoveField(
            model_name='historicalproject',
            name='compute_dec',
        ),
        migrations.RemoveField(
            model_name='historicalproject',
            name='compute_feb',
        ),
        migrations.RemoveField(
            model_name='historicalproject',
            name='compute_jan',
        ),
        migrations.RemoveField(
            model_name='historicalproject',
            name='compute_jul',
        ),
        migrations.RemoveField(
            model_name='historicalproject',
            name='compute_jun',
        ),
        migrations.RemoveField(
            model_name='historicalproject',
            name='compute_mar',
        ),
        migrations.RemoveField(
            model_name='historicalproject',
            name='compute_may',
        ),
        migrations.RemoveField(
            model_name='historicalproject',
            name='compute_nov',
        ),
        migrations.RemoveField(
            model_name='historicalproject',
            name='compute_oct',
        ),
        migrations.RemoveField(
            model_name='historicalproject',
            name='compute_sep',
        ),
        migrations.RemoveField(
            model_name='project',
            name='compute_apr',
        ),
        migrations.RemoveField(
            model_name='project',
            name='compute_aug',
        ),
        migrations.RemoveField(
            model_name='project',
            name='compute_dec',
        ),
        migrations.RemoveField(
            model_name='project',
            name='compute_feb',
        ),
        migrations.RemoveField(
            model_name='project',
            name='compute_jan',
        ),
        migrations.RemoveField(
            model_name='project',
            name='compute_jul',
        ),
        migrations.RemoveField(
            model_name='project',
            name='compute_jun',
        ),
        migrations.RemoveField(
            model_name='project',
            name='compute_mar',
        ),
        migrations.RemoveField(
            model_name='project',
            name='compute_may',
        ),
        migrations.RemoveField(
            model_name='project',
            name='compute_nov',
        ),
        migrations.RemoveField(
            model_name='project',
            name='compute_oct',
        ),
        migrations.RemoveField(
            model_name='project',
            name='compute_sep',
        ),
        migrations.AddField(
            model_name='computeprofile',
            name='compute_apr',
            field=models.CharField(choices=[('128', 128), ('512', 512), ('1024', 1024)], default=('128', 128), max_length=4, verbose_name='April-17'),
        ),
        migrations.AddField(
            model_name='computeprofile',
            name='compute_aug',
            field=models.CharField(choices=[('128', 128), ('512', 512), ('1024', 1024)], default=('128', 128), max_length=4, verbose_name='August-17'),
        ),
        migrations.AddField(
            model_name='computeprofile',
            name='compute_dec',
            field=models.CharField(choices=[('128', 128), ('512', 512), ('1024', 1024)], default=('128', 128), max_length=4, verbose_name='December-17'),
        ),
        migrations.AddField(
            model_name='computeprofile',
            name='compute_feb',
            field=models.CharField(choices=[('128', 128), ('512', 512), ('1024', 1024)], default=('128', 128), max_length=4, verbose_name='February-17'),
        ),
        migrations.AddField(
            model_name='computeprofile',
            name='compute_jan',
            field=models.CharField(choices=[('128', 128), ('512', 512), ('1024', 1024)], default=('128', 128), max_length=4, verbose_name='January-17'),
        ),
        migrations.AddField(
            model_name='computeprofile',
            name='compute_jul',
            field=models.CharField(choices=[('128', 128), ('512', 512), ('1024', 1024)], default=('128', 128), max_length=4, verbose_name='July-17'),
        ),
        migrations.AddField(
            model_name='computeprofile',
            name='compute_jun',
            field=models.CharField(choices=[('128', 128), ('512', 512), ('1024', 1024)], default=('128', 128), max_length=4, verbose_name='June-17'),
        ),
        migrations.AddField(
            model_name='computeprofile',
            name='compute_mar',
            field=models.CharField(choices=[('128', 128), ('512', 512), ('1024', 1024)], default=('128', 128), max_length=4, verbose_name='March-17'),
        ),
        migrations.AddField(
            model_name='computeprofile',
            name='compute_may',
            field=models.CharField(choices=[('128', 128), ('512', 512), ('1024', 1024)], default=('128', 128), max_length=4, verbose_name='May-17'),
        ),
        migrations.AddField(
            model_name='computeprofile',
            name='compute_nov',
            field=models.CharField(choices=[('128', 128), ('512', 512), ('1024', 1024)], default=('128', 128), max_length=4, verbose_name='November-17'),
        ),
        migrations.AddField(
            model_name='computeprofile',
            name='compute_oct',
            field=models.CharField(choices=[('128', 128), ('512', 512), ('1024', 1024)], default=('128', 128), max_length=4, verbose_name='October-17'),
        ),
        migrations.AddField(
            model_name='computeprofile',
            name='compute_sep',
            field=models.CharField(choices=[('128', 128), ('512', 512), ('1024', 1024)], default=('128', 128), max_length=4, verbose_name='September-17'),
        ),
    ]