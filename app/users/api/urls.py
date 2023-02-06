from django.urls import path

from users.api import views

app_name = "user_api"

urlpatterns = [
    path("api/users/", views.UserAPIView.as_view(), name="test"),
]
