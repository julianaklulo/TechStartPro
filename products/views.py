from rest_framework import viewsets

from .serializers import CategorySerializer, ProductSerializer
from .models import Category, Product
from .filters import CategoryFilter, ProductFilter


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer
    filterset_class = CategoryFilter


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('name')
    serializer_class = ProductSerializer
    filterset_class = ProductFilter
