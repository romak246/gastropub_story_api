from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView

from menu.models.dish import Dish
from menu.serializers.dish import DishSerializer
from menu.ulits.pagination import LimitedResultsSetPagination


class DishAPIView(ListAPIView, viewsets.ViewSet):
    """

        Возвращает список блюд

        ---
        * **search** - поиск по названию блюда
        * **category__slug** - фильтр по категории по slug
        * **limit** - пагинация, возвращает указанное количество элементов
    """
    model = Dish
    queryset = Dish.objects.all().exclude(hidden=True)
    serializer_class = DishSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['category__slug']
    search_fields = ['name']
    pagination_class = LimitedResultsSetPagination

