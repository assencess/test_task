# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-31 17:26
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('tapp', '0002_auto_20161031_1634'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='faculty',
            managers=[
                ('students', django.db.models.manager.Manager()),
            ],
        ),
    ]
