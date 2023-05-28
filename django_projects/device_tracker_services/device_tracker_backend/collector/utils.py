from datetime import datetime

from django.utils import timezone
from django.db.models import F
from collector.models import Device, Network, Session


def get_or_create_device(mac_addr, ipv4):
    device, created = Device.objects.get_or_create(
        mac_addr=mac_addr, defaults={"ipv4": ipv4}
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


def maintain_device_sessions(ssid: str, device: Device):
    network = Network.objects.get(ssid=ssid)

    all_active_session = device.sessions.filter(status=Session.StatusType.ACTIVE)
    close_other_networks_sessions(all_active_session, network)
    current_network_active_session = all_active_session.filter(network=network).first()
    if not current_network_active_session:
        new_session = Session.objects.create(network=network, device=device)
        print(f"session for deice: {device} in network: {network} was created: {new_session}")


def maintain_missed_pings(ssid: str, live_mac_addresses: list):
    network = Network.objects.get(ssid=ssid)
    # session must be active; session must belong to exact network
    query = {"session__status": Session.StatusType.ACTIVE, "session__network": network}
    devices = Device.objects.filter(**query)

    # Update `missed_pings` field:
    devices.exclude(mac_addr__in=live_mac_addresses).update(missed_pings=F("missed_pings") + 1)
    devices.filter(mac_addr__in=live_mac_addresses).update(missed_pings=0)

    # Close session for devices that exceed `missed_ping_threshold`
    lost_devices = devices.filter(missed_pings__gte=F("missed_ping_threshold"))
    Session.objects.filter(device__in=lost_devices, network=network, status=Session.StatusType.ACTIVE).\
        update(status=Session.StatusType.CLOSED)
    lost_devices.update(missed_pings=0)
