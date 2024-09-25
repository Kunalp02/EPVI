from django.urls import path
from .views import (
    CategoryListCreateAPIView, CategoryDetailAPIView,
    ProductListCreateAPIView, ProductDetailAPIView,
    CartAPIView,
    OrderListCreateAPIView, OrderUpdateStatusAPIView
)

urlpatterns = [
    path('api/categories/', CategoryListCreateAPIView.as_view(), name='category-list-create'),
    path('api/categories/<int:pk>/', CategoryDetailAPIView.as_view(), name='category-detail'),

    path('api/products/', ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('api/products/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),

    path('api/cart/', CartAPIView.as_view(), name='cart-view-add'),
    path('api/cart/remove/<int:product_id>/', CartAPIView.as_view(), name='cart-item-remove'),

    path('api/orders/', OrderListCreateAPIView.as_view(), name='order-list-create'),
    path('api/orders/update-status/<int:order_id>/', OrderUpdateStatusAPIView.as_view(), name='order-update-status'),
]
