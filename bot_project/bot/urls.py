from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('telegram-bot/', views.my_view),
]
