from django.contrib import admin
from django.urls import path, include

"http://127.0.0.1:8000/tracker/exercises/"
urlpatterns = [
    path("tracker/", include("tracker.urls")),
    path("admin/", admin.site.urls),
]
