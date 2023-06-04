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
    device_mac_addr = CharField(source="device.mac_addr", required=False)
    device_ipv4_addr = IPAddressField(source="device.ipv4", required=False)
    network_ssid = CharField(source="network.ssid", validators=[validate_network_ssid_exists])
    # 5 digits/chars key
    # network_key =

    class Meta:
        model = Session
        fields = ["device_mac_addr", "device_ipv4_addr", "network_ssid"]
