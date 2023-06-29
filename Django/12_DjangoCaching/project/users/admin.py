from django.contrib import admin
from .models import Profile, Product, Order, Shop

admin.site.register(Profile)
admin.site.register(Product)
admin.site.register(Shop)
admin.site.register(Order)


# class OrderInline(admin.StackedInline):
#     model = Order.products.through
#
# @admin.register(Order)
# class OrderAdmin(admin.ModelAdmin):
#     inlines = [
#         OrderInline
#     ]
#     list_display = "delivery_address", "promocode", "created_at", "user_verbose"
#
#     def get_queryset(self, request):
#         return Order.objects.select_related("user").prefetch_related("products")
#
#     def user_verbose(self, obj:Order) -> str:
#         return obj.user.first_name or obj.user.username