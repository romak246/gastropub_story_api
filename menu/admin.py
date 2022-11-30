from django.contrib import admin
from image_cropping import ImageCroppingMixin

from menu.models.category import Category
from menu.models.dish import Dish, DishImage, Serving


class CategoryAdmin(ImageCroppingMixin, admin.ModelAdmin):
    search_fields = ["name"]
    pass


class DishImageAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass


class ServingAdmin(admin.ModelAdmin):
    pass


class ServingAdminInline(admin.TabularInline):
    model = Serving
    extra = 0
    pass


class DishImageInline(ImageCroppingMixin, admin.TabularInline):
    model = DishImage
    min_num = 1
    max_num = 5
    extra = 0


class DishAdmin(ImageCroppingMixin, admin.ModelAdmin):
    autocomplete_fields = ['category']
    inlines = (DishImageInline, ServingAdminInline)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Dish, DishAdmin)
admin.site.register(DishImage, DishImageAdmin)
admin.site.register(Serving, ServingAdmin)
