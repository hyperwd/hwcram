# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-30 00:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vpc', '0035_createip'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='createip',
            name='bandwidth_id',
        ),
        migrations.AddField(
            model_name='createip',
            name='bandwidth_share_name',
            field=models.CharField(blank=True, help_text="<font color='blue'>独享带宽留空</font>，<font color='red'>共享带宽填写</font>", max_length=128, null=True, verbose_name='共享带宽名称'),
        ),
    ]
