from django.urls import path
from collector.views import CreateNetworkView


urlpatterns = [
    path("networks/", CreateNetworkView.as_view(), name="networks_view")
]