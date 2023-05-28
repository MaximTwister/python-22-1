from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from collector.serializers import (
    NetworkSerializer,
    UpdateCreateSessionSerializer,
)
from collector.utils import (
    get_or_create_device,
    maintain_device_sessions,
    maintain_missed_pings,
)


class CreateNetworkView(APIView):
    def post(self, request: Request):

        serializer = NetworkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=HTTP_200_OK)

        return Response(data=serializer.errors, status=HTTP_400_BAD_REQUEST)


class UpdateCreateSessionView(APIView):
    def post(self, request: Request):
        serializer = UpdateCreateSessionSerializer(data=request.data, many=True)

        if serializer.is_valid():
            live_mac_addresses = []
            ssid = ""

            for data in serializer.data:
                data: dict
                mac_addr = data.get("device_mac_addr")
                ipv4 = data.get("device_ipv4_addr")
                ssid = data.get("network_ssid")

                device = get_or_create_device(mac_addr, ipv4)
                maintain_device_sessions(ssid, device)
                live_mac_addresses.append(mac_addr)

            maintain_missed_pings(ssid, live_mac_addresses)
            return Response(data=serializer.data, status=HTTP_200_OK)

        return Response(data=serializer.errors, status=HTTP_400_BAD_REQUEST)
