from rest_framework import viewsets

from .serializers import CategorySerializer
from .models import Category
from .filters import CategoryFilter


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer
    filterset_class = CategoryFilter

# Create your views here.
