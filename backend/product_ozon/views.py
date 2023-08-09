from rest_framework import generics
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        products_count = request.data.get('products_count', 10)
        # Здесь вы можете добавить логику для запуска задачи на парсинг N товаров
        # В качестве заглушки, просто вернем сообщение, что задача запущена
        return Response({'message': f'Запущена задача на парсинг {products_count} товаров'})


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
