from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('telegram-bot/', views.TelegramView),
    path('count/',views.TelegramCount),
]
