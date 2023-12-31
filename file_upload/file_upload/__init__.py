# Loading the Celery app on Django startup
# ensures that the @shared_task decorator will use it correctly.

from .celery import app as celery_app

__all__ = ("celery_app",)