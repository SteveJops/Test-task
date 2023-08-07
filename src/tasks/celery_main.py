from celery import Celery
from celery.schedules import crontab

# celery -A tasks beat --loglevel=INFO

celery_app = Celery('celery_main', include=["tasks"])
celery_app.config_from_object("celeryconfig")

celery_app.conf.beat_schedule = {
    "everyday-task": {
        "task": "tasks.tasks.make_updates",
        "schedule": crontab(minute='*/60'),
    }
}
