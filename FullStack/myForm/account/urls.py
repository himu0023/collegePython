from django.urls import path
from .views import register_view, success_view

app_name = "account"

urlpatterns = [
    path("register/", register_view, name="register"),
    path("success/", success_view, name="success"),
]