# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-31 14:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20161226_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='profile_pics'),
        ),
    ]