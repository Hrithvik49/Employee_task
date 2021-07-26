from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class tasksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tasks'
    verbose_name = _(' Task Management')
