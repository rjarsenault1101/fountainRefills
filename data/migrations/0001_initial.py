# Generated by Django 3.0.5 on 2020-05-03 23:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Datapoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.TextField(default=datetime.datetime(2020, 5, 3, 19, 47, 28, 145140))),
                ('date', models.TextField(default=datetime.date(2020, 5, 3))),
                ('time', models.TextField(default=datetime.time(19, 47, 28, 145140))),
                ('value', models.BigIntegerField()),
                ('cumulative', models.BigIntegerField()),
            ],
        ),
    ]
