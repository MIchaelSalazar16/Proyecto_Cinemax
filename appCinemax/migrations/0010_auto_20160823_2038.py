# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-23 20:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appCinemax', '0009_auto_20160817_1801'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sala',
            name='id',
        ),
        migrations.AlterField(
            model_name='sala',
            name='idSala',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]