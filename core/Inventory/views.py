from rest_framework.generics import (CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView)
from .serializers import CategoryWriteSerializer, CategoryReadSerializer
from .permissions import IsManager
from .models import Category

class CategoryCreateView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryWriteSerializer
    # authentication_classes = [IsManager]


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryReadSerializer

class CategoryDetailView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryReadSerializer

class CategoryUpdateView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryWriteSerializer

# class CategoryDeleteView(DestroyAPIView):
#     queryset = Category.objects.all()
