from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Category, Designer, Product
from .serializer import CategorySerializer, DesignerSerializer, ProductSerializer

class CategoryList(APIView):
    def get(self, data, format=None):
        return Response("")

    def post(self, data, format=None):
        pass

class DesignerList(APIView):
    def get(self, data, format=None):
        pass

    def post(self, data, format=None):
        pass

class ProductList(APIView):
    def get(self, data, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, data, format=None):
        pass

class ProductDetail(APIView):
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Exception, e:
            return Response("Nothing found")


