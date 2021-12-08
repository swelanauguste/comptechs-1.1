from django.urls import path

from . import views

app_name = "users"


urlpatterns = [
    path(
        "profile/edit/<slug:slug>/",
        views.ProfileUpdateView.as_view(),
        name="user-profile-update",
    ),
]
