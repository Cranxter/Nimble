# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-09-30 14:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('X_Home', '0002_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='category',
            field=models.CharField(default='world', max_length=20),
            preserve_default=False,
        ),
    ]
