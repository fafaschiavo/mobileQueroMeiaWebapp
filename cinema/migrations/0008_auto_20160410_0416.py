# -*- coding: utf-8 -*-
# Generated by Django 1.10.dev20160307181939 on 2016-04-10 04:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0007_tickets_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='paid_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
