# -*- coding: utf-8 -*-
# Generated by Django 1.10.dev20160307181939 on 2016-04-09 23:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='hash_id',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
