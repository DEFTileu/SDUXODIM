from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore
from .tasks import notify_upcoming_events

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "default")

    scheduler.add_job(
        notify_upcoming_events,
        trigger="interval",
        minutes=5,
        id="notify_upcoming_events",
        replace_existing=True
    )

    scheduler.start()
    print("✅ Scheduler started...")
