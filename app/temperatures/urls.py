from django.urls import path

from . import views

app_name = "temperatures"


urlpatterns = [
    path("", views.TemperatureListView.as_view(), name="temperature-list"),
    path("add", views.TemperatureCreateView.as_view(), name="temperature-create"),
    path(
        "detail-<int:pk>",
        views.TemperatureDetailView.as_view(),
        name="temperature-detail",
    ),
]
