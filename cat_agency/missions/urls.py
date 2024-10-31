from django.urls import path
from .views import MissionList, MissionDetail

app_name = "missiong"

urlpatterns = [
    path("missions/", MissionList.as_view(), name="mission-list"),
    path("missions/<int:pk>/", MissionDetail.as_view(), name="mission-detail"),
    path("missions/create/", MissionList.as_view(), name="mission-create"),
    path("missions/update/<int:pk>/", MissionDetail.as_view(), name="mission-update"),
    path("missions/delete/<int:pk>/", MissionDetail.as_view(), name="mission-delete"),
]

