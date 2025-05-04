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
        delta = event.start_time - now

        if delta <= timedelta(days=1) and not ticket.reminder_day_sent:
            send_mail(
                subject=f"Напоминание: завтра {event.name}",
                recipients=[ticket.email],
                template_name='emails/reminder_day.html',
                context={
                    'event': event,
                    'user_name': ticket.user_name,
                    'time_left': 'завтра',
                }
            )
            ticket.reminder_day_sent = True
            ticket.save()

        if delta <= timedelta(hours=1) and not ticket.reminder_hour_sent:
            send_mail(
                subject=f"Скоро начнется {event.name}",
                recipients=[ticket.email],
                template_name='emails/reminder_hour.html',
                context={
                    'event': event,
                    'user_name': ticket.user_name,
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
