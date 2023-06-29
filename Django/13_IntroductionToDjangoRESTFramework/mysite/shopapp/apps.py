from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ShopappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shopapp'
    verbose_name = _("shop")
