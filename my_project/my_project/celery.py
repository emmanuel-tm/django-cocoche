import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
# NOTE: evita pasar siempre el módulo de configuración a 'celery'.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_project.settings')

# Creamos la instancia de celery con el nombre del proyecto.
app = Celery('my_project')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()