# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-12 18:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20180812_1827'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='user_cookies',
            field=models.TextField(blank=True, verbose_name='Cookies'),
        ),
    ]
