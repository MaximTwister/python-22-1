import re

from rest_framework.serializers import ValidationError

from collector.models import Network


def validate_network_type(value):
    print(f"[NetworkSerializer] `validate_network_type`: {value} ")
    if value not in dict(Network.NetworkTypes.choices):
        available_choices = [f"{choice} for {value}" for choice, value in Network.NetworkTypes.choices]
        raise ValidationError(f"Invalid network type. Available types are: {available_choices}")


def validate_network_ssid_exists(value):
    if Network.objects.filter(ssid=value).exists():
        return value
    raise ValidationError(f"SSID `{value}` doesn't exists")


def validate_network_ssid_unique(value):
    if Network.objects.filter(ssid=value).exists():
        raise ValidationError(f"SSID `{value}` already exists")



def validate_network_ssid_name(value):
    """
    Validate that a given value is a valid SSID.

    An SSID is valid if it meets the following conditions:
    - it is 2-32 symbols long
    - it doesn't contain any of symbols: ?, ", $, [, ], \, +

    :param value: the value to validate
    :type value: str

    :raise ValidationError: if the value is not valid SSID

    :return: None
    :rvalue: None
    """
    # Check SSID length
    if not (2 <= len(value) <= 32):
        raise ValidationError("SSID must be 2-32 symbols long.")

    # Check invalid symbols (?, ", $, [, ], \, +)
    invalid_chars = r'[?"$\[\]\\+]'
    if re.search(invalid_chars, value):
        raise ValidationError('SSID cannot containt following symbols: ?, ", $, [, ], \, +')
