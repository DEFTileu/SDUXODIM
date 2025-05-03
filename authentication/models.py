# authentication/models.py
from django.db import models
from django.contrib.auth.models import User

class Users(models.Model):
    FACULTY_CHOICES = (
        ('FENS', 'Engineering'),
        ('BS', 'Business'),
        ('EDU', 'Education'),
        ('LSS', 'Law'),
    )

    COURSE_CHOICES = (
        ('1', '1 курс'),
        ('2', '2 курс'),
        ('3', '3 курс'),
        ('4', '4 курс'),
    )
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('club_head', 'HC'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', null=True)
    role = models.CharField(max_length=9, choices=ROLE_CHOICES, default='student')
    course = models.CharField(max_length=1, choices=COURSE_CHOICES)
    faculty = models.CharField(max_length=10, choices=FACULTY_CHOICES)

    def __str__(self):
        return f'{self.user.email} {self.user.username}'
