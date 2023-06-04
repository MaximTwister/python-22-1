from django.db import models
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
    missed_pings = models.IntegerField(default=0)
    missed_pings_threshold = models.IntegerField(default=2)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.ipv4} - {self.mac_addr} - {self.missed_pings}"


class Network(models.Model):

    class NetworkTypes(models.TextChoices):
        # choice, label
        WIFI = "W", "Wi-Fi"
        LAN = "L", "LAN"

    ssid = models.CharField(max_length=32, help_text="The network SSID")
    description = models.CharField(max_length=50)
    network_type = models.CharField(max_length=1, choices=NetworkTypes.choices)
    known_devices = models.ManyToManyField(to="Device", related_name="known_networks")
    added_by = models.ManyToManyField(to=get_user_model(), related_name="added_networks")


class Session(models.Model):

    class StatusType(models.TextChoices):
        ACTIVE = "A", "active session"
        CLOSED = "C", "closed session"
        CLOSED_FORCIBLY = "F", "closed forcibly session"

    start = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    end = models.DateTimeField(null=True)
    network = models.ForeignKey(to="Network", related_name="sessions", on_delete=models.CASCADE)
    device = models.ForeignKey(to="Device", related_name="sessions", on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=StatusType.choices, default=StatusType.ACTIVE)
