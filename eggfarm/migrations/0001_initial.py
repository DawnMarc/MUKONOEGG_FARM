# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-28 15:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Capacity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_of_trays', models.CharField(max_length=50)),
                ('damaged', models.IntegerField()),
                ('Date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_no', models.AutoField(primary_key=True, serialize=False)),
                ('no_of_trays', models.IntegerField(default=0)),
                ('location', models.CharField(default='current location', max_length=100)),
                ('request_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('total_amt_due', models.FloatField(default=0.0, max_length=100)),
                ('status', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Prices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Px_per_Egg', models.FloatField()),
                ('Px_per_Tray', models.FloatField()),
                ('Date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AddField(
            model_name='orders',
            name='Prices',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eggfarm.Prices'),
        ),
        migrations.AddField(
            model_name='orders',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
