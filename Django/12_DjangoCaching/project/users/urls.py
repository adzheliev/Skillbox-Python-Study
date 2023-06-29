from django.urls import path, include
from django.views.generic import TemplateView

from .views import Register, ShopListView




urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    path('register/', Register.as_view(), name='register'),
    path('shop/', ShopListView.as_view(), name='shop'),
]