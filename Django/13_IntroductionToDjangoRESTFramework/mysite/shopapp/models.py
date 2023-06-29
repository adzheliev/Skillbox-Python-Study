from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

def product_preview_directory_path(instance: "Product", filename: str) -> str:
    return "products/product_{pk}/preview/{filename}".format(
        pk=instance.pk,
        filename=filename,
    )

class Shop(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('name'))

class Product(models.Model):
    class Meta:
        ordering = ["name", "price"]
        # db_table = "tech_products"
        verbose_name_plural = _("products")
        verbose_name = _('product')
    name = models.CharField(max_length=100, verbose_name=_('name'))
    description = models.TextField(null=False, blank=True, verbose_name=_('description'))
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2, verbose_name=_('price'))
    discount = models.SmallIntegerField(default=0, verbose_name=_('discount'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))
    archived = models.BooleanField(default=False, verbose_name=_('archived'))
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name=_('created_by'))
    preview = models.ImageField(null=True, blank=True, upload_to=product_preview_directory_path, verbose_name=_('preview'))

    def __str__(self) -> str:
        return f"Product(pk={self.pk}, name={self.name!r})"

def product_images_directory_path(instance: "ProductImage", filename: str) -> str:
    return "products/product_{pk}/images/{filename}".format(
        pk=instance.product.pk,
        filename=filename,
    )

class ProductImage(models.Model):
    class Meta:
        verbose_name_plural = _('product images')
        verbose_name = _('product image')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images", verbose_name=_('product'))
    image = models.ImageField(upload_to=product_images_directory_path, verbose_name=_('image'))
    description = models.CharField(max_length=200, null=False, blank=True, verbose_name=_('description'))

class Order(models.Model):
    delivery_address = models.TextField(null=False, blank=True, verbose_name=_('delivery_address'))
    promocode = models.CharField(max_length=20, null=False, blank=True, verbose_name=_('promocode'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name=_('user'))
    products = models.ManyToManyField(Product, related_name='orders', verbose_name=_('products'))
    receipt = models.FileField(null=True, upload_to='orders/receipts/', verbose_name=_('receipt'))

    class Meta:
        verbose_name_plural = _('orders')
        verbose_name = _('order')


