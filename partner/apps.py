from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class PartnerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'partner'
    verbose_name = _(' Partners')