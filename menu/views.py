from rest_framework.response import Response
from rest_framework.views import APIView

from menu.models import Category
from menu.serializers import CategorySerializer


class CategoryAPIView(APIView):
    model = Category
    serializer_class = CategorySerializer

    def get(self, request):
        categories = Category.objects.all()
        serializer = self.serializer_class(categories, many=True)
        return Response(serializer.data)

