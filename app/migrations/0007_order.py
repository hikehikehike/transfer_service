# Generated by Django 4.1.3 on 2022-12-06 22:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0006_alter_flight_arrival_time_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date_flight", models.DateTimeField()),
                ("number_of_seat", models.IntegerField(default=1)),
                ("name", models.CharField(max_length=255)),
                ("phone_number", models.IntegerField(blank=True, null=True)),
                (
                    "flight",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.flight"
                    ),
                ),
            ],
        ),
    ]
