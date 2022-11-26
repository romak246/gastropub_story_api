from django.db import models
from image_cropping import ImageRatioField


class Category(models.Model):
    name = models.CharField('Название категории', max_length=99)
    image = models.ImageField('Изображение', upload_to='static/menu', height_field=None, width_field=None,
                              max_length=100)
    slug = models.SlugField('Идентификатор', unique=True, max_length=99)
    cropping = ImageRatioField('image', '600x900')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f"{self.name}"
