from django.contrib import admin
from django.urls import path
from .views import ShortLink, RedirectLink

urlpatterns = [
    path('short/', ShortLink.as_view()),
    path('<str:short>/', RedirectLink.as_view()),
]
