from django.shortcuts import render
from django.urls import path
from .views import health_check

urlpatterns = [
    path("healthz", health_check),
]
