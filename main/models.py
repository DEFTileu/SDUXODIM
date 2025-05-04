from django.db import models
from authentication.models import Users

# Create your models here.

class Club(models.Model):
    club_id = models.AutoField(primary_key=True)
    club_name = models.CharField(max_length=20, blank=False)
    subscribers = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.club_name}'

    class Meta:
        app_label = 'main'


class Event(models.Model):
    title = models.CharField(max_length=30, blank=False)
    # organizer = models.CharField(max_length=20, blank=False)
    organizer = models.ForeignKey(Club, to_field='club_id', on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(blank=False)
    location = models.CharField(max_length=40, null=True)


    def __str__(self):
        return f'{self.title} - {self.organizer}'


class Ticket(models.Model):
    user = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True)
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True)
    notified_1day = models.BooleanField(default=False)
    notified_1hour = models.BooleanField(default=False)


class Media(models.Model):
    image = models.ImageField(upload_to="main/static/images/")