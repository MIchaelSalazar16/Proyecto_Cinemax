# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-17 15:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appCinemax', '0002_auto_20160817_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelicula',
            name='imagenPortada',
            field=models.ImageField(blank=True, null=True, upload_to=b'/static/imagenes'),
        ),
    ]
