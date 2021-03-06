# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-25 11:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_email', models.EmailField(blank=True, default=None, max_length=254, null=True)),
                ('customer_name', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('customer_phone', models.CharField(blank=True, default=None, max_length=48, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('comments', models.TextField(blank=True, default=None, null=True)),
            ],
            options={
                'verbose_name': 'Замовлення',
                'verbose_name_plural': 'Замовлення',
            },
        ),
        migrations.CreateModel(
            name='ProductinOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_email', models.EmailField(blank=True, default=None, max_length=254, null=True)),
                ('customer_name', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('customer_phone', models.CharField(blank=True, default=None, max_length=48, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товари',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=24, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Статус замовленяя',
                'verbose_name_plural': 'Статуси замовленнь',
            },
        ),
        migrations.AddField(
            model_name='productinorder',
            name='is_active',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Status'),
        ),
        migrations.AddField(
            model_name='productinorder',
            name='order',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Order'),
        ),
        migrations.AddField(
            model_name='productinorder',
            name='product',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Product'),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Status'),
        ),
    ]
