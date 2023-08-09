from rest_framework import generics
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
import json
from rest_framework.views import APIView
from rest_framework import status


class LoadDataFromJSON(APIView):
    def post(self, request):
        json_file_path = "product_ozon/migrations/json_items/all_products.json"

        with open(json_file_path, 'r') as json_file:
            data = json.load(json_file)

        products = data.get('product', [])

        for product_data in products:
            try:
                name = product_data.get('name', '')
                price = int(product_data.get('price', '0'))
                discount = product_data.get('discount', '')
                image_url = product_data.get('image_url', '')
                code_product = int(product_data.get('code_product', '0'))

                # Проверяем, существует ли продукт с таким кодом в базе данных
                existing_product = Product.objects.filter(code_product=code_product).first()

                # Если продукта с таким кодом нет, и image_url не пустой, добавляем его
                if not existing_product and image_url:
                    Product.objects.create(
                        name=name,
                        price=price,
                        discount=discount,
                        image_url=image_url,
                        code_product=code_product
                    )
                elif existing_product:
                    if existing_product.price != price:
                        existing_product.price = price
                    if existing_product.image_url != image_url:
                        existing_product.image_url = image_url
                    existing_product.save()
            except Exception as e:
                return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"message": "Data loaded successfully"}, status=status.HTTP_201_CREATED)



class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
