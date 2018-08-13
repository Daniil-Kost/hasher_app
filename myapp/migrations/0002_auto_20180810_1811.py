# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-10 18:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hashes',
            options={'verbose_name': 'Hash', 'verbose_name_plural': 'Hashes'},
        ),
        migrations.AlterField(
            model_name='hashes',
            name='related_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_hashes', to='myapp.UserProfile', verbose_name='Related User'),
        ),
    ]
