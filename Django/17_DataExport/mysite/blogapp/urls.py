from django.urls import path, include
from django.contrib import admin
from .views import ArticleListView

app_name = 'blogapp'

urlpatterns = [
    path("list/", ArticleListView.as_view(), name="article_list"),
    ]
