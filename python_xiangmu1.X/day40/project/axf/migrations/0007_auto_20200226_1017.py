# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2020-02-26 02:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('axf', '0006_categoriegroup_childgroup'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('sex', models.BooleanField()),
                ('phoneNum', models.CharField(max_length=20)),
                ('postCode', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=500)),
                ('province', models.CharField(max_length=40)),
                ('city', models.CharField(max_length=40)),
                ('county', models.CharField(max_length=40)),
                ('street', models.CharField(max_length=40)),
                ('detailAddress', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'addresses',
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField()),
                ('isOrder', models.BooleanField(default=True)),
                ('isCheck', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'carts',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('orderId', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('price', models.FloatField()),
                ('flag', models.IntegerField(default=0)),
                ('createTime', models.DateTimeField(auto_now_add=True)),
                ('lastTime', models.DateTimeField(auto_now=True)),
                ('isDelete', models.BooleanField(default=False)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='axf.Address')),
            ],
            options={
                'db_table': 'orders',
            },
            managers=[
                ('orders1', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('phoneNum', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('passwd', models.CharField(default=None, max_length=20, null=True)),
                ('tokenValue', models.CharField(max_length=100)),
                ('headImg', models.CharField(max_length=200)),
                ('integral', models.IntegerField(default=0)),
                ('vipLevel', models.IntegerField(default=0)),
                ('createTime', models.DateTimeField(auto_now_add=True)),
                ('lastLoginTime', models.DateTimeField(auto_now=True)),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='axf.User'),
        ),
        migrations.AddField(
            model_name='cart',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='axf.Order'),
        ),
        migrations.AddField(
            model_name='cart',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='axf.Product'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='axf.User'),
        ),
        migrations.AddField(
            model_name='address',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='axf.User'),
        ),
    ]
