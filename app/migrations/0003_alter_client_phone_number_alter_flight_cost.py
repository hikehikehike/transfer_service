# Generated by Django 4.1.3 on 2022-12-02 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_alter_flight_cost"),
    ]

    operations = [
        migrations.AlterField(
            model_name="client",
            name="phone_number",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="flight",
            name="cost",
            field=models.IntegerField(default=False),
            preserve_default=False,
        ),
    ]