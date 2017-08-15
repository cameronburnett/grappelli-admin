# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-27 17:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20170725_1405'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComputeProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slots_or_hosts', models.CharField(choices=[('Slots', 'Slots'), ('Hosts', 'Hosts'), ('Both', 'Both')], max_length=2)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='compute_profile',
            field=models.ManyToManyField(to='project.ComputeProfile'),
        ),
    ]