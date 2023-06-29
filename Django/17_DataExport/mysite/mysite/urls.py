"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
import debug_toolbar
from django.contrib.sitemaps.views import sitemap
from app_news.sitemap import NewsSitemap

sitemaps = {
    'news': NewsSitemap
}


def trigger_error(request):
    division_by_zero = 1 / 0


urlpatterns = [
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    path('shop/', include('shopapp.urls')),
    path('news/', include('app_news.urls')),
    path('home_sale/', include('home_sale.urls')),
    path('rss/', include('app_rss.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('blog/', include('blogapp.urls')),
    path('req/', include('requestdataapp.urls')),
    path('app_pages/', include('app_pages.urls')),
    path('i18n', include('django.conf.urls.i18n')),
    path('accounts/', include('myauth.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('api/', include('myapiapp.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
    path('sentry-debug/', trigger_error),
]

if settings.DEBUG:
    urlpatterns.extend(
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    )
    urlpatterns.extend(
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    )
