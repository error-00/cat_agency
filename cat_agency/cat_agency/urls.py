from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("cats/", include("cats.urls", namespace="cats")),
    # path("missions/", include("misisons.urls", namespace="missions")),
]

