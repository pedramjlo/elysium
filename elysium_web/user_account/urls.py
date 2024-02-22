from django.urls import path

from .views import register_view, login_view, out, ProfileView





urlpatterns = [
    path("register/", register_view, name='register'),
    path("login/", login_view, name='login'),
    path("profile/<int:pk>", ProfileView.as_view(), name='profile'),
    path("logout/", out, name='logout'),


]