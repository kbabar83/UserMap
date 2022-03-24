from django.urls import path

from user.views import UsersMapView, UserHomeView

app_name = "user"

urlpatterns = [
    path("", UserHomeView.as_view()),
    path("map/", UsersMapView.as_view()),
]
