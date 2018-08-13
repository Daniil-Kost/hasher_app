# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-12 20:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20180812_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='user_city',
            field=models.CharField(blank=True, default=None, max_length=256, null=True, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='user_cookies',
            field=models.TextField(blank=True, default=None, null=True, verbose_name='Cookies'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='user_country',
            field=models.CharField(blank=True, default=None, max_length=256, null=True, verbose_name='Country'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='user_timezone',
            field=models.CharField(blank=True, default=None, max_length=256, null=True, verbose_name='Timezone'),
        ),
    ]
