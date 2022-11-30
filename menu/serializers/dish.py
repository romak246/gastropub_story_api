from rest_framework import serializers

from menu.models.dish import Dish, DishImage, Serving
from menu.ulits.cropper import Cropper


class DishImageSerializer(serializers.ModelSerializer):
    img = serializers.SerializerMethodField()

    @staticmethod
    def get_img(instance):
        return Cropper(instance).get_cropped_image()

    class Meta:
        model = DishImage
        fields = ("img",)


class ServingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serving
        fields = '__all__'


class DishSerializer(serializers.ModelSerializer):
    images = DishImageSerializer(many=True)
    servings = ServingSerializer(many=True)

    class Meta:
        model = Dish
        fields = ("slug", "name", "ingredients", "images", "servings", "category")
