# Generated by Django 4.1.3 on 2022-12-07 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0014_alter_client_phone_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="client",
            name="phone_number",
            field=models.IntegerField(default=380),
        ),
    ]
