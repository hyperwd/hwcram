# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-25 08:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vpc', '0013_auto_20170925_1614'),
    ]

    operations = [
        migrations.RenameField(
            model_name='createip',
            old_name='bandwidth_id',
            new_name='bandwidth_share_id',
        ),
        migrations.AddField(
            model_name='createip',
            name='project_id',
            field=models.CharField(max_length=40, null=True, verbose_name='项目ID'),
        ),
    ]
