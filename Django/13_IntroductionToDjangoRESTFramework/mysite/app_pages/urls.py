from django.urls import path
from django.views.decorators.cache import cache_page

from app_pages.views import translation_example, greetings_page, welcome, main_page

app_name = "app_pages"

urlpatterns = [
    path("", translation_example, name='example'),
    path("greetings/", greetings_page, name='greetings_page'),
    path("welcome/", cache_page(30)(welcome), name='welcome'),
    path("main_page/", cache_page(40)(main_page), name='main_page'),
]