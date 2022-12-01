from django.db import models
from image_cropping import ImageRatioField

from menu.models.category import Category
from menu.ulits.cyrillic_slugify import slugify

VolumeChoices = (
    ("gram", "Г"),
    ("milliliter", "Мл"),
)


class Dish(models.Model):
    name = models.CharField('Название', max_length=99, blank=False, unique=True)
    ingredients = models.CharField('Состав блюда', max_length=99)
    slug = models.SlugField('Идентификатор', unique=True, max_length=99, blank=True)
    category = models.ForeignKey(Category, verbose_name="category", related_name="dishes",
                                 on_delete=models.CASCADE, null=True, blank=True)
    hidden = models.BooleanField('Скрыть блюдо из меню', default=False)
    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Dish, self).save(*args, **kwargs)


class DishImage(models.Model):
    image = models.ImageField('Изображение', upload_to='static/menu', height_field=None, width_field=None,
                              max_length=100)
    cropping = ImageRatioField('image', '600x600')
    dish = models.ForeignKey(Dish, verbose_name="dish", related_name="images",
                             on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Изображение блюда'
        verbose_name_plural = 'Изображение блюд'

    def __str__(self):
        return f"Изображение блюда {self.dish.name}"


class Serving(models.Model):
    name = models.CharField('Название сервировки', max_length=99, blank=True)
    description = models.CharField('Описание сервировки', max_length=99, blank=True)

    volume = models.FloatField('Объем', blank=False)

    volume_unit = models.CharField(null=False, verbose_name='Единицы измерения объема', choices=VolumeChoices,
                                   blank=False, max_length=100)
    price = models.FloatField('Цена', blank=False)
    dish = models.ForeignKey(Dish, verbose_name="dish", related_name="servings",
                             on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Сервировка'
        verbose_name_plural = 'Сервировки'

    def __str__(self):
        return f"Вариант серивировки блюда {self.dish.name}"
