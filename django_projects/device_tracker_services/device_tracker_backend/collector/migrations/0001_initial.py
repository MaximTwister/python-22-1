# Generated by Django 4.2.1 on 2023-05-21 09:11

import collector.validators
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Device",
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
                ("ipv4", models.GenericIPAddressField(protocol="IPv4")),
                ("mac_addr", models.CharField(max_length=17)),
                ("name", models.CharField(max_length=20)),
                (
                    "device_type",
                    models.CharField(
                        choices=[
                            ("SM", "Smartphone"),
                            ("TB", "Tablet"),
                            ("LP", "Laptop"),
                            ("PC", "Personal Computer"),
                            ("WT", "Watch"),
                            ("GC", "Gaming Console"),
                        ],
                        max_length=2,
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="devices",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Network",
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
                (
                    "ssid",
                    models.CharField(
                        help_text="The network SSID",
                        max_length=32,
                    ),
                ),
                ("description", models.CharField(max_length=50)),
                (
                    "network_type",
                    models.CharField(
                        choices=[("W", "Wi-Fi"), ("L", "LAN")], max_length=1
                    ),
                ),
                (
                    "added_by",
                    models.ManyToManyField(
                        related_name="added_networks", to=settings.AUTH_USER_MODEL
                    ),
                ),
                (
                    "known_devices",
                    models.ManyToManyField(
                        related_name="known_networks", to="collector.device"
                    ),
                ),
            ],
        ),
    ]
