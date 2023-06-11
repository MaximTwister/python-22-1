from rest_framework.serializers import (
    ModelSerializer,
    Serializer,
    CharField,
    IPAddressField,
    SerializerMethodField,
)
from rest_framework.exceptions import ValidationError

from collector.models import (
    Network,
    Session, Device,
)
from collector.validators import (
    validate_network_ssid_name,
    validate_network_type,
    validate_network_ssid_unique,
    validate_network_ssid_exists,
)
from collector.utils import (
    get_secret_key,
    get_or_create_device,
    get_device_session,
)


class NetworkSerializer(ModelSerializer):
    network_type = CharField(validators=[validate_network_type])
    ssid = CharField(validators=[validate_network_ssid_name, validate_network_ssid_unique])

    class Meta:
        model = Network
        read_only_fields = ["secret_key"]
        fields = ["ssid", "description", "network_type", "secret_key"]

        extra_kwargs = {
            "description": {"required": False, "default": "No description."}
        }

    def to_internal_value(self, data):
        internal_data = super().to_internal_value(data)
        secret_key = get_secret_key(model=Network)
        if not secret_key:
            raise ValidationError({"error": "Network `secret_key` was not generated"})

        internal_data["secret_key"] = secret_key
        return internal_data


class DeviceSerializer(ModelSerializer):
    name = CharField(required=False)
    device_type = CharField(required=False)

    class Meta:
        model = Device
        read_only_fields = ["secret_key"]
        fields = ["ipv4", "mac_addr", "secret_key", "name", "device_type"]


class SessionSerializer(ModelSerializer):
    device = DeviceSerializer()
    network_ssid = CharField(source="network.ssid", validators=[validate_network_ssid_exists])

    class Meta:
        model = Session
        fields = ["device", "network_ssid"]

    def create(self, validated_data):
        print(f"`SessionSerializer.create()` with validated_data: {validated_data}")
        device_data = validated_data.pop("device")
        network_data = validated_data.pop("network")
        device = get_or_create_device(**device_data)
        session = get_device_session(device=device, **network_data)
        return session


class NetworkActiveDevicesSerializer(ModelSerializer):
    active_devices = SerializerMethodField()

    class Meta:
        model = Network
        fields = ["ssid", "description", "network_type", "active_devices"]

    @staticmethod
    def get_active_devices(obj: Network):
        print(f"`NetworkActiveDevicesSerializer.get_active_devices()` with obj: {obj}")
        active_sessions = Session.objects.filter(network=obj, status=Session.StatusType.ACTIVE)
        active_devices = Device.objects.filter(sessions__in=active_sessions)
        return DeviceSerializer(active_devices, many=True).data


class SecretKeySerializer(Serializer):
    secret_key = CharField(required=True)
