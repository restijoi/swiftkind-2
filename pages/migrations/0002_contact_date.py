# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-21 05:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 21, 5, 47, 10, 214332, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
