from django.urls import path
from home_sale.views import ContactsView, AboutUsView, HousesListView, NewsListView, NewsItemDetailView
from home_sale.feeds import LatestNewsFeed
from django.contrib.sitemaps.views import sitemap
from home_sale.sitemap import NewsSitemap

app_name = "home_sale"
sitemaps = {
    'news': NewsSitemap
}

urlpatterns = [
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('about-us/', AboutUsView.as_view(), name='about-us'),
    path('houses-list/', HousesListView.as_view(), name='houses-list'),
    path('news-list/', NewsListView.as_view(), name='news-list'),
    path('rss/', LatestNewsFeed()),
    path('<int:pk>', NewsItemDetailView.as_view(), name='news-item'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap')
    ]
