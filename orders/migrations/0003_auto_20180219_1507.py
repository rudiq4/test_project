# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-19 13:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20180208_1728'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Замовлення', 'verbose_name_plural': 'Замовлення'},
        ),
        migrations.AlterModelOptions(
            name='productinorder',
            options={'verbose_name': 'Товар в замовленні', 'verbose_name_plural': 'Товари у замовленні'},
        ),
        migrations.AlterField(
            model_name='order',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Створено'),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer_address',
            field=models.CharField(blank=True, default=None, max_length=128, null=True, verbose_name='Адрес покупця'),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer_email',
            field=models.EmailField(blank=True, default=None, max_length=254, null=True, verbose_name='E-mail покупця'),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer_name',
            field=models.CharField(blank=True, default=None, max_length=64, null=True, verbose_name='Імя покупця'),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer_phone',
            field=models.CharField(blank=True, default=None, max_length=48, null=True, verbose_name='Тел. номер покупця'),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Сумарна ціна'),
        ),
        migrations.AlterField(
            model_name='order',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Оновлено'),
        ),
        migrations.AlterField(
            model_name='productinorder',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Створено'),
        ),
        migrations.AlterField(
            model_name='productinorder',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Оновлено'),
        ),
        migrations.AlterField(
            model_name='status',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Створено'),
        ),
        migrations.AlterField(
            model_name='status',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Оновлено'),
        ),
    ]
