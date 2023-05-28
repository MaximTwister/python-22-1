from rest_framework.serializers import (
    ModelSerializer,
    CharField,
    IPAddressField,
)

from collector.models import (
    Network,
    Session,
)
from collector.validators import (
    validate_network_ssid_name,
    validate_network_type,
    validate_network_ssid_unique,
    validate_network_ssid_exists,
)


class NetworkSerializer(ModelSerializer):
    network_type = CharField(validators=[validate_network_type])
    ssid = CharField(validators=[validate_network_ssid_name, validate_network_ssid_unique])

    class Meta:
        model = Network
        fields = ["ssid", "description", "network_type"]

        extra_kwargs = {
            "description": {"required": False, "default": "No description."}
        }


class UpdateCreateSessionSerializer(ModelSerializer):
    device_mac_addr = CharField(source="device.mac_addr", write_only=True)
    device_ip_addr = IPAddressField(source="device.ipv4", write_only=True)
    network_ssid = CharField(source="network.ssid", write_only=True, validators=[validate_network_ssid_exists])

    class Meta:
        model = Session
        fields = ["device_mac_addr", "device_ip_addr", "network_ssid"]
