# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-17 17:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appCinemax', '0006_auto_20160817_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelicula',
            name='imagenPortada',
            field=models.ImageField(upload_to=b'images/'),
        ),
    ]