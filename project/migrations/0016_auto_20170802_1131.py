# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-02 18:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0015_auto_20170802_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computeprofile',
            name='compute_apr',
            field=models.CharField(max_length=3, verbose_name='April-17'),
        ),
        migrations.AlterField(
            model_name='computeprofile',
            name='compute_aug',
            field=models.CharField(max_length=3, verbose_name='August-17'),
        ),
        migrations.AlterField(
            model_name='computeprofile',
            name='compute_dec',
            field=models.CharField(max_length=3, verbose_name='December-17'),
        ),
        migrations.AlterField(
            model_name='computeprofile',
            name='compute_feb',
            field=models.CharField(max_length=3, verbose_name='February-17'),
        ),
        migrations.AlterField(
            model_name='computeprofile',
            name='compute_jan',
            field=models.CharField(max_length=3, verbose_name='January-17'),
        ),
        migrations.AlterField(
            model_name='computeprofile',
            name='compute_jul',
            field=models.CharField(max_length=3, verbose_name='July-17'),
        ),
        migrations.AlterField(
            model_name='computeprofile',
            name='compute_jun',
            field=models.CharField(max_length=3, verbose_name='June-17'),
        ),
        migrations.AlterField(
            model_name='computeprofile',
            name='compute_mar',
            field=models.CharField(max_length=3, verbose_name='March-17'),
        ),
        migrations.AlterField(
            model_name='computeprofile',
            name='compute_may',
            field=models.CharField(max_length=3, verbose_name='May-17'),
        ),
        migrations.AlterField(
            model_name='computeprofile',
            name='compute_nov',
            field=models.CharField(max_length=3, verbose_name='November-17'),
        ),
        migrations.AlterField(
            model_name='computeprofile',
            name='compute_oct',
            field=models.CharField(max_length=3, verbose_name='October-17'),
        ),
        migrations.AlterField(
            model_name='computeprofile',
            name='compute_sep',
            field=models.CharField(max_length=3, verbose_name='September-17'),
        ),
        migrations.AlterField(
            model_name='historicalcomputeprofile',
            name='compute_apr',
            field=models.CharField(max_length=3, verbose_name='April-17'),
        ),
        migrations.AlterField(
            model_name='historicalcomputeprofile',
            name='compute_aug',
            field=models.CharField(max_length=3, verbose_name='August-17'),
        ),
        migrations.AlterField(
            model_name='historicalcomputeprofile',
            name='compute_dec',
            field=models.CharField(max_length=3, verbose_name='December-17'),
        ),
        migrations.AlterField(
            model_name='historicalcomputeprofile',
            name='compute_feb',
            field=models.CharField(max_length=3, verbose_name='February-17'),
        ),
        migrations.AlterField(
            model_name='historicalcomputeprofile',
            name='compute_jan',
            field=models.CharField(max_length=3, verbose_name='January-17'),
        ),
        migrations.AlterField(
            model_name='historicalcomputeprofile',
            name='compute_jul',
            field=models.CharField(max_length=3, verbose_name='July-17'),
        ),
        migrations.AlterField(
            model_name='historicalcomputeprofile',
            name='compute_jun',
            field=models.CharField(max_length=3, verbose_name='June-17'),
        ),
        migrations.AlterField(
            model_name='historicalcomputeprofile',
            name='compute_mar',
            field=models.CharField(max_length=3, verbose_name='March-17'),
        ),
        migrations.AlterField(
            model_name='historicalcomputeprofile',
            name='compute_may',
            field=models.CharField(max_length=3, verbose_name='May-17'),
        ),
        migrations.AlterField(
            model_name='historicalcomputeprofile',
            name='compute_nov',
            field=models.CharField(max_length=3, verbose_name='November-17'),
        ),
        migrations.AlterField(
            model_name='historicalcomputeprofile',
            name='compute_oct',
            field=models.CharField(max_length=3, verbose_name='October-17'),
        ),
        migrations.AlterField(
            model_name='historicalcomputeprofile',
            name='compute_sep',
            field=models.CharField(max_length=3, verbose_name='September-17'),
        ),
    ]
