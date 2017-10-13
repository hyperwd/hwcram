# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-30 09:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vpc', '0040_auto_20170930_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createip',
            name='region',
            field=models.CharField(choices=[('cn-north-1', '华北1'), ('cn-east-2', '华东2'), ('cn-south-1', '华南1')], max_length=32, null=True, verbose_name='区域'),
        ),
        migrations.AlterField(
            model_name='vpc',
            name='region',
            field=models.CharField(choices=[('cn-north-1', '华北1'), ('cn-east-2', '华东2'), ('cn-south-1', '华南1')], default='cn-north-1', max_length=32, verbose_name='区域'),
        ),
    ]
