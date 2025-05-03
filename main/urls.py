from django.contrib import admin
from django.urls import path, include
from main.views import index_page, about_page
from authentication.views import login_page,register_page

urlpatterns = [
    path('', index_page, name = 'index'),
    path('about/', about_page, name = 'about'),
]
