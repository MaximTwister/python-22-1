from django.urls import path
from collector.views import (
    CreateNetworkView,
    UpdateCreateSessionView,
)


urlpatterns = [
    path("networks/", CreateNetworkView.as_view(), name="networks_view"),
    path("device-sessions/", UpdateCreateSessionView.as_view(), name="device_sessions_view"),
]
