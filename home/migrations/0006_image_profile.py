# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-13 11:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instapp', '0003_auto_20180308_1142'),
        ('home', '0005_follow'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='instapp.Profile'),
        ),
    ]
