# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-26 06:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='illustration',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
