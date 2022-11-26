from django.contrib import admin
from image_cropping import ImageCroppingMixin
from menu.models import Category


class CategoryAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass


admin.site.register(Category, CategoryAdmin)
