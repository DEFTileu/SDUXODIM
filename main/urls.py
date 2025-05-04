from django.contrib import admin
from django.urls import path, include
from main.views import index_page, about_page, fortest

urlpatterns = [
    path('', index_page, name = 'index'),
    path('about/', about_page, name = 'about'),
    path('fortest/', fortest, name = 'fortest'),
]
