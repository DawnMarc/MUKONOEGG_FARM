# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-03 16:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eggfarm', '0002_auto_20180331_0101'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('invoice_no', models.AutoField(primary_key=True, serialize=False)),
                ('orders', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eggfarm.Orders')),
                ('prices', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eggfarm.Prices')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
