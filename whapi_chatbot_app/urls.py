
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('executar/', views.executar_request, name='executar_request'),
    path('healthz/', views.health_check, name='health_check'),
]