# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-14 12:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('csViewer', '0004_auto_20160914_1633'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='c_minus_r',
            new_name='i_minus_r',
        ),
    ]