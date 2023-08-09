from django.urls import path
from .views import ProductListCreateView, ProductDetailView
from .views import LoadDataFromJSON

urlpatterns = [
    path('v1/products/', ProductListCreateView.as_view(),
          name='product-list-create'),
    path('v1/products/<int:pk>/', ProductDetailView.as_view(),
          name='product-detail'),
    path('v1/load_data/', LoadDataFromJSON.as_view(), name='load-data'), 
]
