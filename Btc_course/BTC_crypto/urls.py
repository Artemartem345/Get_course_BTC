from .views import * 
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('Crypto_BTC/', GetCourseBTC.as_view()),
    path('Crypto_LTC/', GetCourseLTC.as_view()),
]