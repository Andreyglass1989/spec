# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-02-28 15:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recovery_info', '0003_delete_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(unique=True)),
                ('image', models.ImageField(upload_to=b'')),
                ('typeFailure', models.ManyToManyField(to='recovery_info.TypeDamage')),
            ],
        ),
    ]