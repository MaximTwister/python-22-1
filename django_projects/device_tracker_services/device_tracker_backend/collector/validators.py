from django.core.exceptions import ValidationError
import re


def validate_ssid(value):
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
        raise ValidationError(
            message="SSID must be 2-32 symbols long."
        )

    # Check invalid symbols (?, ", $, [, ], \, +)
    invalid_chars = r'[?"$\[\]\\+]'
    if re.search(invalid_chars, value):
        raise ValidationError(
            message='SSID cannot containt following symbols: ?, ", $, [, ], \, +'
        )
