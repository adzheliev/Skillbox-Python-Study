from django.db import models
from django.urls import reverse


class HouseType(models.Model):
    name = models.CharField(max_length=128, verbose_name='name')

    class Meta:
        verbose_name = 'house_type'
        verbose_name_plural = 'house_types'

    def __str__(self):
        return self.name

class RoomsQuantity(models.Model):
    rooms = models.IntegerField(verbose_name='rooms', default=0)

    class Meta:
        verbose_name = 'room'
        verbose_name_plural = 'rooms'



class House(models.Model):
    title = models.CharField(max_length=128, verbose_name='title')
    description = models.TextField(verbose_name='description')
    price = models.IntegerField(verbose_name='price', default=0)
    is_published = models.BooleanField(default=False)
    type = models.ForeignKey(HouseType, on_delete=models.CASCADE, related_name='house', null=True)
    rooms = models.ForeignKey(RoomsQuantity, on_delete=models.CASCADE, related_name='house', null=True)
    published_at = models.DateTimeField(verbose_name='published_at', null=True)

    class Meta:
        verbose_name = 'house'
        verbose_name_plural = 'houses'

    def __str__(self):
        return self.title

class NewsItem(models.Model):
    title = models.CharField(max_length=128, verbose_name='title')
    text = models.TextField(verbose_name='text')
    is_published = models.BooleanField(default=False)
    description = models.TextField(verbose_name='description', default='')
    published_at = models.DateTimeField(verbose_name='published_at', null=True)


    def get_absolute_url(self):
        return reverse('news-item', args=[str(self.id)])

    class Meta:
        verbose_name = 'news'
        verbose_name_plural = 'news'