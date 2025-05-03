# authentication/signals.py
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Users

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Users.objects.create(
            user=instance,
            username=instance.username,
            email=instance.email,
            password=instance.password,  # Пароль лучше не хранить в явном виде
            role='student',  # Установите значение по умолчанию
            course='1',  # Установите значение по умолчанию
            faculty='FENS'  # Установите значение по умолчанию
        )

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()