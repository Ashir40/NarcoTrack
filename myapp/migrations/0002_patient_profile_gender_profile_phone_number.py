# Generated by Django 4.1.5 on 2023-05-18 08:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="patient",
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
                ("name", models.CharField(max_length=200)),
                ("father_name", models.CharField(max_length=200)),
                ("gender", models.CharField(default="Unknown", max_length=200)),
                ("cnic", models.CharField(max_length=200)),
                ("phone_number", models.CharField(max_length=200)),
                ("drug_addiction", models.CharField(max_length=200)),
                ("plan", models.CharField(max_length=200)),
                ("fees", models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name="profile",
            name="gender",
            field=models.CharField(default="Unknown", max_length=200),
        ),
        migrations.AddField(
            model_name="profile",
            name="phone_number",
            field=models.CharField(
                blank=True,
                max_length=13,
                validators=[
                    django.core.validators.RegexValidator(
                        message="Phone number must be entered in the format: '+923117121727'. 11 digits required.",
                        regex="^\\+?\\d{11}$",
                    )
                ],
            ),
        ),
    ]