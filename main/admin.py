from django.contrib import admin
from main.models import Event, Club, Media, Ticket

# Register your models here.
admin.site.register(Event)
admin.site.register(Club)
admin.site.register(Media)
admin.site.register(Ticket)