# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2023-03-30 08:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_user', '0006_auto_20230330_0802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminuser',
            name='just_datetime',
            field=models.DateTimeField(null=True),
        ),
    ]