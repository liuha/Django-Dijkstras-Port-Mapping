# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-05 16:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NetworkPort',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('floor', models.IntegerField(default=3)),
                ('port', models.IntegerField(default=1)),
                ('room', models.CharField(default=b'unknown', max_length=25)),
                ('section', models.CharField(default=b'unknown', max_length=25)),
                ('x_coord', models.IntegerField(null=True)),
                ('y_coord', models.IntegerField(null=True)),
            ],
        ),
    ]