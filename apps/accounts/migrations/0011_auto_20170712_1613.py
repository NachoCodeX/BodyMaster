# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-12 16:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20170712_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
