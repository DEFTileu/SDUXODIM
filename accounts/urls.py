
from django.urls import path, include
from accounts.views import profile,add_event

urlpatterns = [
    path('', profile, name='profile'),
    path('add_event.html',add_event,name='add_event'),

]
