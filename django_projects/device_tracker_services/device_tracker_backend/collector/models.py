from django.db import models
from collector.validators import validate_ssid
from django.contrib.auth import get_user_model

class Device(models.Model):

    class DeviceTypes(models.TextChoices):
        SMARTPHONE = "SM", "Smartphone"
        TABLET = "TB", "Tablet",
        LAPTOP = "LP", "Laptop",
        PC = "PC", "Personal Computer",
        WATCH = "WT", "Watch",
        GAME_CONSOLE = "GC", "Gaming Console"

    ipv4 = models.GenericIPAddressField(protocol="IPv4")
    mac_addr = models.CharField(max_length=17)
    name = models.CharField(max_length=20)
    device_type = models.CharField(max_length=2, choices=DeviceTypes.choices)
    owner = models.ForeignKey(
        to=get_user_model(),
        related_name="devices",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )


class Network(models.Model):

    class NetworkTypes(models.TextChoices):
        # choice, label
        WIFI = "W", "Wi-Fi"
        LAN = "L", "LAN"

    ssid = models.CharField(max_length=32, help_text="The network SSID", validators=[validate_ssid])
    description = models.CharField(max_length=50)
    network_type = models.CharField(max_length=1, choices=NetworkTypes.choices)
    known_devices = models.ManyToManyField(to="Device", related_name="known_networks")
    added_by = models.ManyToManyField(to=get_user_model(), related_name="added_networks")


class Session(models.Model):
    pass
