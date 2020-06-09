from django.db import models


# Create your models here.
class Photo(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    Img = models.ImageField(upload_to='images/', verbose_name='Фото')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')

class Meta:
    verbose_name = 'Фотография'
    verbose_name_plural = 'Фотография'
