from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("collector/api/v1/", include("collector.urls"))
]
