from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from django.core.cache import cache



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, verbose_name=_('user'))
    balance = models.IntegerField(null=True, blank=True, default=0, verbose_name=_('balance'))
    promo = models.CharField(max_length=500, blank=True, verbose_name=_('promo'))
    promo_cache_key = 'promo'
    cache.get_or_set(promo_cache_key, promo, 30*60)
    offers = models.CharField(max_length=500, blank=True, verbose_name=_('offers'))
    offers_cache_key = 'offers'
    cache.get_or_set(offers_cache_key, offers, 30 * 60)
    user_account_cache_data = {
        promo_cache_key: promo,
        offers_cache_key: offers
    }
    cache.set_many(user_account_cache_data)

    class Meta:
        verbose_name_plural = _('profiles')
        verbose_name = _('profile')

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self) -> str:
        return str(self.user)

class Shop(models.Model):
    name = models.CharField(max_length=500, blank=True, verbose_name=_('name'))

    class Meta:
        verbose_name_plural = _('shops')
        verbose_name = _('shop')

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    class Meta:
        ordering = ["name", "price"]
        verbose_name_plural = _('products')
        verbose_name = _('product')
    name = models.CharField(max_length=100, verbose_name=_('name'))
    description = models.TextField(null=False, blank=True, verbose_name=_('description'))
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2, verbose_name=_('price'))
    discount = models.SmallIntegerField(default=0, verbose_name=_('discount'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))
    archived = models.BooleanField(default=False, verbose_name=_('archived'))
    shop = models.ForeignKey(Shop, on_delete=models.PROTECT, null=True, verbose_name=_('shop'))


    def __str__(self) -> str:
        return self.name

class Order(models.Model):
    delivery_address = models.TextField(null=False, blank=True, verbose_name=_('delivery_address'))
    promocode = models.CharField(max_length=20, null=False, blank=True, verbose_name=_('promocode'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))
    user = models.ForeignKey(Profile, related_name='orders', on_delete=models.PROTECT, verbose_name=_('user'))
    products = models.ManyToManyField(Product, related_name='orders', verbose_name=_('products'))

    class Meta:
        verbose_name_plural = _('orders')
        verbose_name = _('order')

    def __str__(self) -> str:
        return str(self.created_at)


