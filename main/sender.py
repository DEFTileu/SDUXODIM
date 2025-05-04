import threading
import time
from django.utils import timezone
from datetime import timedelta
from .models import Ticket
from utils.utils import send_mail


def check_and_send_reminders():
    print("Запуск напоминаний...")
    now = timezone.now()
    for ticket in Ticket.objects.select_related('event'):
        event = ticket.event
        delta = event.date - now

        if delta <= timedelta(days=1) and not ticket.notified_1day:
            send_mail(
                subject=f"Напоминание: завтра {event.title}",
                recipients=[ticket.user.email],
                template_name='Notification/reminder_day.html',
                context={
                    'event': event,
                    'user_name': ticket.user.username,
                    'time_left': 'завтра',
                }
            )
            ticket.reminder_day_sent = True
            ticket.save()

        if delta <= timedelta(hours=1) and not ticket.notified_1hour:
            send_mail(
                subject=f"Скоро начнется {event.title}",
                recipients=[ticket.user.email],
                template_name='Notification/reminder_day.html',
                context={
                    'event': event,
                    'user_name': ticket.user.username,
                    'time_left': 'через час',
                }
            )
            ticket.reminder_hour_sent = True
            ticket.save()


def start_reminder_loop():
    def loop():
        while True:
            check_and_send_reminders()
            time.sleep(300)  # 300 секунд = 5 минут

    threading.Thread(target=loop, daemon=True).start()
