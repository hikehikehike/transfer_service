# Generated by Django 4.1.3 on 2022-12-07 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0009_remove_order_name_remove_order_phone_number_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="client",
            name="phone_number",
            field=models.IntegerField(),
        ),
    ]