# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-03-04 18:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recovery_info', '0004_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='os',
        ),
        migrations.AlterField(
            model_name='file',
            name='image',
            field=models.ImageField(upload_to='static/images/'),
        ),
        migrations.DeleteModel(
            name='OperatingSystem',
        ),
    ]
