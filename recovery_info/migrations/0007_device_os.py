# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-03-04 18:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recovery_info', '0006_operatingsystem'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='os',
            field=models.ManyToManyField(to='recovery_info.OperatingSystem'),
        ),
    ]