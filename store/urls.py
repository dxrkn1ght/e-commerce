from django.urls import path
from .views import product_list, product_detail, category_detail


urlpatterns = [
    path('', product_list, name='product-list'),
    path('product/<int:pk>/', product_detail, name='product-detail'),
    path('category/<int:pk>/', category_detail, name='category_detail'),
]