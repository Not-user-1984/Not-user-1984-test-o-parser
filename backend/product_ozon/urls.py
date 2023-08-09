from django.urls import path
from .views import ProductListCreateView, ProductDetailView

urlpatterns = [
    path('v1/products/', ProductListCreateView.as_view(),
          name='product-list-create'),
    path('v1/products/<int:pk>/', ProductDetailView.as_view(),
          name='product-detail'),
]
