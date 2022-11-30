from rest_framework import serializers

from menu.models.category import Category
from menu.ulits.cropper import Cropper


class CategorySerializer(serializers.ModelSerializer):
    cropped_img = serializers.SerializerMethodField()

    @staticmethod
    def get_cropped_img(instance):
        return Cropper(instance).get_cropped_image()

    class Meta:
        model = Category
        fields = ("slug", "name", "cropped_img")
