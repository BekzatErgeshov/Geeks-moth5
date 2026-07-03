from django.urls import path

from app.settings.views import (
    CalculatorAPIView,
    CategoryAPIView,
    ProductListAPIView,
    TemperatureAPIView,
)

urlpatterns = [
    path("category-list", CategoryAPIView.as_view(), name="category-list"),
    path("product-list", ProductListAPIView.as_view(), name="product-list"),
    path("calculator", CalculatorAPIView.as_view(), name="calculator"),
    path("temperature", TemperatureAPIView.as_view(), name="temperature"),
]
