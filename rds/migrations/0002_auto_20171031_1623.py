# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-31 08:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rds', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rds',
            name='rds_type',
            field=models.CharField(choices=[('master', '主实例'), ('slave', '备实例'), ('readreplica', '只读实例')], max_length=20, null=True, verbose_name='类型'),
        ),
    ]
