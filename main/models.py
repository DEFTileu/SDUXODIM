from django.db import models

# Create your models here.

class Club(models.Model):
    club_id = models.AutoField(primary_key=True)
    club_name = models.CharField(max_length=20, blank=False)
    subscribers = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.club_name}'


class Event(models.Model):
    title = models.CharField(max_length=30, blank=False)
    # organizer = models.CharField(max_length=20, blank=False)
    organizer = models.ForeignKey(Club, to_field='club_id', on_delete=models.SET_NULL, null=True)
    date = models.DateField(blank=False)


    def __str__(self):
        return f'{self.title} - {self.organizer}'


class Media(models.Model):
    image = models.ImageField(upload_to="main/static/images/")