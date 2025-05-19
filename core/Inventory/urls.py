from django.urls import path
from .views import CategoryCreateView, CategoryListView, CategoryDetailView, CategoryUpdateView

urlpatterns = [
    path('category/create/', CategoryCreateView.as_view(), name='category-create'),
    path('category/list/', CategoryListView.as_view(), name='Category-list'),
    path('category/<int:pk>/detail/', CategoryDetailView.as_view(), name='category-detail'),
    path('category/<int:pk>/update/', CategoryUpdateView.as_view(), name='category-update')
]