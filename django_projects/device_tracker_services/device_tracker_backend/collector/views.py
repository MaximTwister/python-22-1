from drf_yasg.utils import swagger_auto_schema
from drf_yasg.openapi import Parameter, IN_BODY, TYPE_STRING
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
)

from collector.models import Network
from collector.serializers import (
    NetworkSerializer,
    SessionSerializer,
    NetworkActiveDevicesSerializer,
    SecretKeySerializer,
)
from collector.utils import maintain_missed_pings


class NetworkCreateView(APIView):

    @swagger_auto_schema(request_body=NetworkSerializer)
    def post(self, request: Request):

        serializer = NetworkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=HTTP_200_OK)

        return Response(data=serializer.errors, status=HTTP_400_BAD_REQUEST)


class SessionUpdateCreateView(APIView):

    @swagger_auto_schema(
        request_body=SessionSerializer,
        responses={
            200: SessionSerializer,
            400: "Bad Request - Validation Failed"
        }
    )
    def post(self, request: Request):
        serializer = SessionSerializer(data=request.data, many=True)

        if not serializer.is_valid():
            return Response(data=serializer.errors, status=HTTP_400_BAD_REQUEST)
        serializer.save()

        live_mac_addresses = []
        ssid = ""

        for data in serializer.data:
            device = data.get("device")
            ssid = data.get("network_ssid")
            live_mac_addresses.append(device.get("mac_addr"))

        maintain_missed_pings(ssid, live_mac_addresses)
        return Response(data=serializer.data, status=HTTP_200_OK)


class NetworkActiveDevicesGetView(APIView):

    @swagger_auto_schema(
        request_body=SecretKeySerializer,
        responses={
            200: NetworkActiveDevicesSerializer(),
            400: "Bad Request - No secret key provided in response body",
            404: "Not Found - No network found with provided secret key"
        }
    )
    def post(self, request):
        secret_key = request.data.get("secret_key")
        if not secret_key:
            return Response({"error": "secret_key was not provided"}, status=HTTP_400_BAD_REQUEST)

        try:
            network = Network.objects.get(secret_key=secret_key)
        except Network.DoesNotExist:
            return Response({"error": "Network not found"}, status=HTTP_404_NOT_FOUND)

        serializer = NetworkActiveDevicesSerializer(network)
        return Response(serializer.data)


# TODO: create endpoint to set devices Name and/or type with device id
