# Generated by Django 4.1.3 on 2022-12-02 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0004_alter_car_capacity"),
    ]

    operations = [
        migrations.AddField(
            model_name="car",
            name="name",
            field=models.CharField(default="Car", max_length=255),
        ),
    ]