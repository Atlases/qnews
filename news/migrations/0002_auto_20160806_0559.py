# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-08-06 05:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='body',
            new_name='content',
        ),
    ]
