from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # Add the registration URL below
    path('register/', views.register, name='register'),
]