from django.db import models
from image_cropping import ImageRatioField
from menu.ulits.cyrillic_slugify import slugify


class Category(models.Model):
    name = models.CharField('Название категории', max_length=99, unique=True)
    image = models.ImageField('Изображение', upload_to='static/menu', height_field=None, width_field=None,
                              max_length=100)
    slug = models.SlugField('Идентификатор', unique=True, max_length=99, blank=True)
    cropping = ImageRatioField('image', '600x670')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
