# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-27 18:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0008_auto_20170727_1107'),
    ]

    operations = [
        migrations.AddField(
            model_name='computeprofile',
            name='compute_size',
            field=models.CharField(choices=[('128', 128), ('512', 512), ('1028', 1028)], default=128, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='computeprofile',
            name='compute_apr',
            field=models.CharField(max_length=4, verbose_name='April-17'),
        ),
        migrations.AlterField(
            model_name='computeprofile',
            name='compute_aug',
            field=models.CharField(max_length=4, verbose_name='August-17'),
        ),
        migrations.AlterField(
            model_name='computeprofile',
            name='compute_dec',
            field=models.CharField(max_length=4, verbose_name='December-17'),
        ),
        migrations.AlterField(
            model_name='computeprofile',
            name='compute_feb',
            field=models.CharField(max_length=4, verbose_name='February-17'),
        ),
        migrations.AlterField(
            model_name='computeprofile',
            name='compute_jan',
            field=models.CharField(max_length=4, verbose_name='January-17'),
        ),
        migrations.AlterField(
            model_name='computeprofile',
            name='compute_jul',
            field=models.CharField(max_length=4, verbose_name='July-17'),
        ),
        migrations.AlterField(
            model_name='computeprofile',
            name='compute_jun',
            field=models.CharField(max_length=4, verbose_name='June-17'),
        ),
        migrations.AlterField(
            model_name='computeprofile',
            name='compute_mar',
            field=models.CharField(max_length=4, verbose_name='March-17'),
        ),
        migrations.AlterField(
            model_name='computeprofile',
            name='compute_may',
            field=models.CharField(max_length=4, verbose_name='May-17'),
        ),
        migrations.AlterField(
            model_name='computeprofile',
            name='compute_nov',
            field=models.CharField(max_length=4, verbose_name='November-17'),
        ),
        migrations.AlterField(
            model_name='computeprofile',
            name='compute_oct',
            field=models.CharField(max_length=4, verbose_name='October-17'),
        ),
        migrations.AlterField(
            model_name='computeprofile',
            name='compute_sep',
            field=models.CharField(max_length=4, verbose_name='September-17'),
        ),
        migrations.AlterField(
            model_name='computeprofile',
            name='slots_or_hosts',
            field=models.CharField(choices=[('Slots', 'Slots'), ('Hosts', 'Hosts'), ('Both', 'Both')], max_length=10),
        ),
    ]
