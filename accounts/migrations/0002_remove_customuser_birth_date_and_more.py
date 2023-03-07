# Generated by Django 4.1.7 on 2023-03-07 00:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customuser",
            name="birth_date",
        ),
        migrations.AddField(
            model_name="customuser",
            name="date_of_birth",
            field=models.DateField(
                default=datetime.datetime(2023, 3, 7, 0, 44, 9, 174282)
            ),
        ),
    ]
