# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-24 06:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appCinemax', '0015_auto_20160824_0617'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pelicula',
            name='id',
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='idPelicula',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]