from .views import *
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('Crypto/', GetCourseBTC.as_view()),
]