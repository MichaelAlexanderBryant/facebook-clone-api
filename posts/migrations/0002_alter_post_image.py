# Generated by Django 4.1.7 on 2023-03-07 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="static/post_images/"
            ),
        ),
    ]
