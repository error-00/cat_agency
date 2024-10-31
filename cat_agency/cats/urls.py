from django.urls import path
from .views import SpyCatCreate, SpyCatList, SpyCatDetail

app_name = "cats"

urlpatterns = [
    path("cats/", SpyCatList.as_view(), name="cat-list"),
    path("cats/<int:pk>/", SpyCatDetail.as_view(), name="cat-detail"),
    path("cats/create/", SpyCatCreate.as_view(), name="cat-create"),
    path("cats/update/<int:pk>/", SpyCatDetail.as_view(), name="cat-update"),
    path("cats/delete/<int:pk>/", SpyCatDetail.as_view(), name="cat-delete"),
]

