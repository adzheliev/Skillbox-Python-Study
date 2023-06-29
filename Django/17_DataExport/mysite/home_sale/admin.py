
from django.contrib import admin
from home_sale.models import House, HouseType, RoomsQuantity, NewsItem

admin.site.register(House)
admin.site.register(HouseType)
admin.site.register(RoomsQuantity)
admin.site.register(NewsItem)