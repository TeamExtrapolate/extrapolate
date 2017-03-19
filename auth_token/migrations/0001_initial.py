# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-19 20:13
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthToken',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('key', models.CharField(max_length=40, verbose_name='Key')),
            ],
            options={
                'verbose_name_plural': 'Tokens',
                'verbose_name': 'Token',
                'abstract': False,
            },
        ),
    ]
