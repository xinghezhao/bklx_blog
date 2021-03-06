# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-16 06:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20161215_1515'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='achievement',
            name='content',
            field=models.TextField(default=33, max_length=500, verbose_name='\u6218\u5f79\u7b80\u4ecb'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='achievement',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='achievement',
            name='title',
            field=models.CharField(max_length=20, verbose_name='\u6307\u6325\u6218\u5f79'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='person',
            name='person',
            field=models.TextField(max_length=300, verbose_name='\u4e2a\u4eba\u4ecb\u7ecd'),
        ),
    ]
