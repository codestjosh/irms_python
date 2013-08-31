from rest_framework.serializers import ModelSerializer
from .models import Category, Designer, Product

class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category

class DesignerSerializer(ModelSerializer):

    class Meta:
        model = Designer

class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product