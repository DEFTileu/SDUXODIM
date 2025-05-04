from django.db import models

class Users(models.Model):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('club_head', 'Head of Club'),
    )

    COURSE_CHOICES = (
        ('1', '1 курс'),
        ('2', '2 курс'),
        ('3', '3 курс'),
        ('4', '4 курс'),
    )
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=16, blank=False)
    password = models.CharField(max_length=16, blank=False)
    email = models.EmailField(unique=True, blank=False)
    course = models.CharField(max_length=1, choices=COURSE_CHOICES, blank=False)
    faculty = models.CharField(max_length=16, blank=False)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student', blank=False)

    last_login = models.DateTimeField(blank=False, null=True)

    def __str__(self):
        return f'{self.username} ({self.role})'

