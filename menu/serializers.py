from PIL import Image
from rest_framework import serializers
from menu.models import Category
from menu.utils import Cropper


class CategorySerializer(serializers.ModelSerializer):
    cropped_img = serializers.SerializerMethodField()

    @staticmethod
    def get_cropped_img(instance):
        return Cropper(instance).get_cropped_image()

    class Meta:
        model = Category
        fields = ("slug", "name", "cropped_img")
