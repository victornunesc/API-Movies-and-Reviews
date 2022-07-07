from django.urls import path
from users.views import UserLogin, UserView

urlpatterns = [
    path("users/register/", UserView.as_view()),
    path("users/login/", UserLogin.as_view()),
]
