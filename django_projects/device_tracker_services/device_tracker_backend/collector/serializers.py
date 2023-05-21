from rest_framework.serializers import (
    ModelSerializer,
)

from collector.models import Network


class NetworkSerializer(ModelSerializer):

    class Meta:
        model = Network
        field = []
