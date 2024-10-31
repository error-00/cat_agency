from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("cats.urls", namespace="cats")),
    path("api/", include("missions.urls", namespace="missions")),
]

