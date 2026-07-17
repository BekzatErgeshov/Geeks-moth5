from django.urls import path
from rest_framework.routers import DefaultRouter

from app.settings.views import CategoryViewSet, ProductViewSet 

router = DefaultRouter()
router.register("category", CategoryViewSet, basename="category")
router.register("product", ProductViewSet, basename="product")

urlpatterns = [
    # path("category-list", CategoryAPIView.as_view(), name="category-list"),
    # path("product-list", ProductListAPIView.as_view(), name="product-list"),
    # path("product-create", ProductCreateAPIView.as_view(), name="create"),
    # path("product-read/<int:pk>/", ProductReadAPIView.as_view(), name="read"),
    # path("product-update/<int:pk>/", ProductUpdateAPIView.as_view(), name="update"),
    # path("product-delete/<int:pk>/", ProductDeleteAPIView.as_view(), name="delete"),
]

urlpatterns = router.urls