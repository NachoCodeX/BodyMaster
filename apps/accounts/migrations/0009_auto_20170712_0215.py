# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-12 02:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_compra'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articulo',
            name='img',
        ),
        migrations.AlterField(
            model_name='articulo',
            name='dec',
            field=models.TextField(blank=True, null=True),
        ),
    ]
