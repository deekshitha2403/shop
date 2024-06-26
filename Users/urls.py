from django.urls import path
from .views import register_user, login_user, logout_user

urlpatterns = [

    path("", register_user),
    path("login-user/", login_user),
    path("logout-user/", logout_user)
]