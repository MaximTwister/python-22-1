from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from collector.views import (
    NetworkCreateView,
    SessionUpdateCreateView,
    NetworkActiveDevicesGetView
)

info = openapi.Info(
    title="Device Collector",
    default_version="v0.9",
    description="Documentation for Device Collector Project",
)

swagger_view = get_schema_view(info=info, public=True, permission_classes=[permissions.AllowAny])

urlpatterns = [
    path("swagger/", swagger_view.with_ui("swagger", cache_timeout=0)),
    path("redoc/", swagger_view.with_ui("redoc", cache_timeout=0)),

    path("networks/", NetworkCreateView.as_view(), name="networks_view"),
    path("create-session/", SessionUpdateCreateView.as_view(), name="create_session_view"),
    path("network-active-sessions/", NetworkActiveDevicesGetView.as_view(), name="network_active_sessions_view"),
]
