# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-15 07:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20161215_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='content',
            field=models.TextField(max_length=400, verbose_name='\u4e2a\u4eba\u8bc4\u4ef7'),
        ),
    ]
