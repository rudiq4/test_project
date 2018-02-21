# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-19 13:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20180219_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimage',
            name='main_picture',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='syte_description',
            field=models.TextField(blank=True, default=None, null=True, verbose_name='Опис на сайті'),
        ),
    ]
