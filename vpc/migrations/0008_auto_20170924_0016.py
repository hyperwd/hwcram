# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-23 16:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vpc', '0007_auto_20170924_0014'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vpc',
            old_name='pubclicip_id',
            new_name='publicip_id',
        ),
    ]