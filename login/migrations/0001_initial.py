# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-10 17:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=200)),
                ('auth12', models.CharField(max_length=16)),
            ],
        ),
    ]