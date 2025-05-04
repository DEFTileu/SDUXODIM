from django.contrib import admin
from django.urls import path, include
from main.views import index_page, about_page,logout_view, booking_page, booking_view, place_order, event_detail

urlpatterns = [
    path('', index_page, name = 'index'),
    path('about/', about_page, name = 'about'),
    path('logout/', logout_view, name='logout'),
    # path('booking/', booking_page, name='booking')
    path('booking/<int:event_id>/', booking_view, name='booking'),
    # path('generate_qr/', generate_qr, name='generate_qr'),
    path('place_order/', place_order, name='place_order'),



]
