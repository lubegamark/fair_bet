# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 15:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('betting', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gamescore',
            name='game',
        ),
        migrations.RemoveField(
            model_name='score',
            name='game',
        ),
        migrations.RemoveField(
            model_name='prediction',
            name='score',
        ),
        migrations.AddField(
            model_name='game',
            name='away_score',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='game',
            name='home_score',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='prediction',
            name='away_score',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='prediction',
            name='home_score',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='GameScore',
        ),
        migrations.DeleteModel(
            name='Score',
        ),
    ]
