from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView, ListView

from home_sale.models import House, NewsItem


class ContactsView(TemplateView):
    template_name = "home_sale/contacts.html"


class AboutUsView(TemplateView):
    template_name = "home_sale/about-us.html"


class HousesListView(ListView):
    template_name = 'home_sale/houses-list.html'
    context_object_name = "houses"
    queryset = House.objects.select_related('type', 'rooms')


class NewsListView(ListView):
    template_name = 'home_sale/news-list.html'
    context_object_name = "news"
    queryset = NewsItem.objects.all()\
        .filter(is_published=True)\
        .only('title', 'text')


class NewsItemDetailView(generic.DetailView):
    model = NewsItem
    template_name = 'home_sale/newsitem_detail.html'