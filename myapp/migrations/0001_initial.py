# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-10 09:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hashes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(default=' ', max_length=256, verbose_name='Word')),
                ('hash_md5', models.TextField(blank=True, verbose_name='Hashes_md5')),
                ('hash_sha1', models.TextField(blank=True, verbose_name='Hashes_sha1')),
                ('hash_sha224', models.TextField(blank=True, verbose_name='Hashes_sha224')),
                ('hash_sha256', models.TextField(blank=True, verbose_name='Hashes_sha256')),
                ('hash_sha512', models.TextField(blank=True, verbose_name='Hashes_sha512')),
                ('file', models.FileField(upload_to='uploads')),
            ],
            options={
                'verbose_name': 'Hashes',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Profile',
            },
        ),
        migrations.CreateModel(
            name='Vocabulary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(default=None, max_length=256, verbose_name='Word')),
            ],
            options={
                'verbose_name': 'Vocabulary',
                'verbose_name_plural': 'Vocabularies',
            },
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user_vocabulary',
            field=models.ManyToManyField(blank=True, to='myapp.Vocabulary', verbose_name='Vocabularies'),
        ),
        migrations.AddField(
            model_name='hashes',
            name='related_user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_hashes', to='myapp.UserProfile', verbose_name='Related User'),
        ),
    ]
