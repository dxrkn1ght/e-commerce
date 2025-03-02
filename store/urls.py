from django.urls import path
from .views import product_list, product_detail, catalog_list, catalog_detail


urlpatterns = [
    path('', product_list, name='product-list'),
    path('<int:pk>/', product_detail, name='product-detail'),
    path('', catalog_list, name='category-list'),
    path('<int:pk>/', catalog_detail, name='category-detail'),
]