# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-16 11:47
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20170916_1157'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='body2',
        ),
        migrations.AddField(
            model_name='news',
            name='intro',
            field=models.TextField(default='请编剧简介'),
        ),
        migrations.AlterField(
            model_name='news',
            name='body',
            field=ckeditor.fields.RichTextField(default='请编辑内容'),
        ),
    ]
