# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2023-03-30 08:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_user', '0010_auto_20230330_0818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminuser',
            name='created_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='adminuser',
            name='updated_at',
            field=models.DateTimeField(null=True),
        ),
    ]
