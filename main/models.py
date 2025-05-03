from django.db import models

# Create your models here.

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30, blank=False)
    organizer = models.CharField(max_length=20, blank=False)
    date = models.DateField(blank=False)

    def __str__(self):
        return f'{self.title} - {self.organizer}'