# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-02-28 14:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prices', '0002_auto_20170226_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='name',
            field=models.TextField(unique=True),
        ),
    ]
