from datetime import datetime
from random import choices
from typing import Optional, Type
from string import digits, ascii_uppercase

from django.utils import timezone
from django.db.models import F
from rest_framework.exceptions import ValidationError

from collector.models import Device, Network, Session


def get_or_create_device(mac_addr: str, ipv4: str) -> Device:
    secret_key = get_secret_key(model=Device)
    if not secret_key:
        raise ValidationError({"error": "Device `secret_key` was not generated"})

    device, created = Device.objects.get_or_create(
        mac_addr=mac_addr,
        defaults={"ipv4": ipv4, "secret_key": secret_key}
    )

    if not created and device.ipv4 != ipv4:
        device.ipv4 = ipv4
        device.save()
        print(f"Device: {device} was updated with new ip: {ipv4}")
    else:
        print(f"Device: {device} was created")

    return device


def close_other_networks_sessions(active_session, network):
    active_session.exclude(network=network).update(
        end=datetime.now(tz=timezone.utc),
        status=Session.StatusType.CLOSED_FORCIBLY
    )


def get_device_session(device: Device, ssid: str) -> Session:
    network = Network.objects.get(ssid=ssid)

    # Get all active sessions for the device
    active_sessions = device.sessions.filter(status=Session.StatusType.ACTIVE)

    # Close inactive sessions that are not related to the current network
    close_other_networks_sessions(active_sessions, network)

    # Check if there is already an active session for this device on the network
    active_session = active_sessions.filter(network=network).first()
    result = "already created"

    if not active_session:
        active_session = Session.objects.create(network=network, device=device)
        result = "created"

    print(f"session for deice: {device} in network: {network} was {result}: {active_session}")
    return active_session


def maintain_missed_pings(ssid: str, live_mac_addresses: list):
    network = Network.objects.get(ssid=ssid)
    # session must be active; session must belong to exact network
    query = {"sessions__status": Session.StatusType.ACTIVE, "sessions__network": network}
    devices = Device.objects.filter(**query)

    # Update `missed_pings` field:
    devices.exclude(mac_addr__in=live_mac_addresses).update(missed_pings=F("missed_pings") + 1)
    devices.filter(mac_addr__in=live_mac_addresses).update(missed_pings=0)

    # Close session for devices that exceed `missed_ping_threshold`
    lost_devices = list(devices.filter(missed_pings__gte=F("missed_pings_threshold")))
    Session.objects.filter(
        device__in=lost_devices,
        network=network,
        status=Session.StatusType.ACTIVE
    ).update(status=Session.StatusType.CLOSED)
    Device.objects.filter(pk__in=[device.pk for device in lost_devices]).update(missed_pings=0)


def get_secret_key(model: Type[Network] | Type[Device], tries_threshold=100) -> Optional[str]:
    print(f"{model} generation key ...")
    for gen_try in range(1, tries_threshold):
        secret_key = "".join(choices(ascii_uppercase + digits, k=4))
        if not model.objects.filter(secret_key=secret_key).exists():
            print(f"{model} key was generated: {secret_key} with {gen_try} try")
            return secret_key

    print(f"ERROR: failed to generate a unique secret_key for {model} with {tries_threshold} tries")
    return None
