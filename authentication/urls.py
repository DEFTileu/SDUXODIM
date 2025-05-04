from django.urls import path
from . import views  # или нужный модуль
from accounts.views import profile


urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('register/', views.register_page, name='register'),

    path('profile/', profile, name='profile')
]

