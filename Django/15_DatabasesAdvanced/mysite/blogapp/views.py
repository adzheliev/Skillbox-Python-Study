from django.shortcuts import render
from django.views.generic import ListView
from .models import Article


class ArticleListView(ListView):
    template_name = 'blogapp/article_list.html'
    context_object_name = "articles"
    queryset = Article.objects.all()\
        .select_related('author', 'category')\
        .prefetch_related('tags')\
        .defer('content')