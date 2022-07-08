from django.urls import path
from users.views import UserIdView, UserLogin, UserRegisterView, UserView

urlpatterns = [
    path("users/register/", UserRegisterView.as_view()),
    path("users/login/", UserLogin.as_view()),
    path("users/", UserView.as_view()),
    path("users/<user_id>", UserIdView.as_view()),
]
