# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-03 20:24
from __future__ import unicode_literals

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        ('betting', '0002_auto_20171027_1543'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPoints',
            fields=[
            ],
            options={
                'verbose_name': 'Points',
                'verbose_name_plural': 'Points',
                'proxy': True,
                'indexes': [],
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='game',
            name='away_score',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='home_score',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
