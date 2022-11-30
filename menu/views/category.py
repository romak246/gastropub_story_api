from rest_framework import viewsets
from rest_framework.generics import ListAPIView

from menu.models.category import Category
from menu.serializers.category import CategorySerializer


class CategoryAPIView(ListAPIView, viewsets.ViewSet):
    """

        Возвращает список категорий

        ---
    """
    model = Category
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

