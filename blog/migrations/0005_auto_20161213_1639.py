# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-13 08:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blog_introduce'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(default=1, upload_to='photos'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='introduce',
            field=models.TextField(max_length=70, verbose_name='\u4ecb\u7ecd'),
        ),
    ]
