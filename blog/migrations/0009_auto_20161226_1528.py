# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-26 09:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20161226_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FileField(blank=True, default='profile_pic', null=True, upload_to='profile_pics'),
        ),
    ]
