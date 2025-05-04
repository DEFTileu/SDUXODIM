
from django.urls import path, include
from accounts.views import profile
from authentication.views import login_page,register_page

urlpatterns = [
    path('', profile, name='profile'),

]
