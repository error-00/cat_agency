from django.urls import path
from .views import MissionList, MissionDetail, TargetList, TargetDetail

app_name = "missiong"

urlpatterns = [
    path("missions/", MissionList.as_view(), name="mission-list"),
    path("missions/<int:pk>/", MissionDetail.as_view(), name="mission-detail"),
    path("missions/create/", MissionList.as_view(), name="mission-create"),
    path("missions/update/<int:pk>/", MissionDetail.as_view(), name="mission-update"),
    path("missions/delete/<int:pk>/", MissionDetail.as_view(), name="mission-delete"),

    path("targets/", TargetList.as_view(), name="target-list"),
    path("targets/<int:pk>/", TargetDetail.as_view(), name="target-detail"),
    path("targets/create/", TargetList.as_view(), name="target-create"),
    path("targets/update/<int:pk>/", TargetDetail.as_view(), name="target-update"),
    path("targets/delete/<int:pk>/", TargetDetail.as_view(), name="target-delete"),
]

