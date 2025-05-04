from django.utils.timezone import now
from datetime import timedelta
from django.core.mail import send_mail
from .models import Ticket

def notify_upcoming_events():
    current_time = now()

    # Уведомления за 1 день
    target_1day = current_time + timedelta(hours=24)
    tickets_1day = Ticket.objects.filter(
        event__start_time__range=(target_1day - timedelta(minutes=1), target_1day + timedelta(minutes=1)),
        notified_1day=False
    )

    for ticket in tickets_1day:
        user = ticket.user
        event = ticket.event

        send_mail(
            subject=f'Напоминание: событие "{event.name}" через 1 день!',
            message=f'Привет, {user.username}! Событие "{event.name}" начнётся завтра — {event.start_time}.',
            from_email='noreply@example.com',
            recipient_list=[user.email]
        )
        ticket.notified_1day = True
        ticket.save()

    # Уведомления за 1 час
    target_1hour = current_time + timedelta(hours=1)
    tickets_1hour = Ticket.objects.filter(
        event__start_time__range=(target_1hour - timedelta(minutes=1), target_1hour + timedelta(minutes=1)),
        notified_1hour=False
    )

    for ticket in tickets_1hour:
        user = ticket.user
        event = ticket.event

        send_mail(
            subject=f'Скоро начнётся: "{event.name}" через 1 час!',
            message=f'Привет, {user.username}! Через час начнётся событие "{event.name}" — {event.start_time}.',
            from_email='noreply@example.com',
            recipient_list=[user.email]
        )
        ticket.notified_1hour = True
        ticket.save()
