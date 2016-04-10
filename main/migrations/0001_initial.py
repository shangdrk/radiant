# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-10 11:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Connection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('one_to_two', models.TextField()),
                ('two_to_one', models.TextField()),
                ('user_one', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='initiator', to=settings.AUTH_USER_MODEL)),
                ('user_two', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
