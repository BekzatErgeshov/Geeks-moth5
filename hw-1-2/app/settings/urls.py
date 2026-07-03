from django.urls import path

from app.settings.views import (
    CalculatorAPIView,
    CategoryAPIView,
    ProductListAPIView,
    ProductCreateAPIView,
    ProductRetrieveAPIView,
    ProductUpdateAPIView,
    ProductDestroyAPIView,
    TemperatureAPIView,
)

urlpatterns = [
    path("category-list", CategoryAPIView.as_view(), name="category-list"),
    path("product-list", ProductListAPIView.as_view(), name="product-list"),
    path("product-create", ProductCreateAPIView.as_view(), name="product-create"),
    path("product-detail/<int:pk>", ProductRetrieveAPIView.as_view(), name="product-detail"),
    path("product-update/<int:pk>", ProductUpdateAPIView.as_view(), name="product-update"),
    path("product-delete/<int:pk>", ProductDestroyAPIView.as_view(), name="product-delete"),
    path("calculator", CalculatorAPIView.as_view(), name="calculator"),
    path("temperature", TemperatureAPIView.as_view(), name="temperature"),
]
