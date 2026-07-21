from rest_framework.generics import ListAPIView, CreateAPIView,\
RetrieveAPIView, UpdateAPIView, DestroyAPIView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.core.cache import cache

from app.settings.models import Category, Product
from app.settings.serializers import CategorySerializers, ProductSerializer

# class CategoryAPIView(ListAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializers
# 
# @method_decorator(cache_page(60*5), name="dispatch")
# class ProductListAPIView(ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
# 
# class ProductCreateAPIView(CreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
# 
#     def perform_create(self, serializer):
#         serializer.save()
#         cache.clear() 
# 
# class ProductReadAPIView(RetrieveAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
# 
# class ProductUpdateAPIView(UpdateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
# 
#     def perform_create(self, serializer):
#         serializer.save()
#         cache.clear()
# 
# class ProductDeleteAPIView(DestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
# 
#     def perform_create(self, serializer):
#         serializer.save()
#         cache.clear()


from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from app.pagination import ProductPagination
from app.filters import ProductFilter

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

class CategoryViewSet(
    mixins.ListModelMixin,
    GenericViewSet
):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

@method_decorator(cache_page(60*5), name="dispatch")
class ProductViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination
    filterset_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    ]
    filterset_class = ProductFilter
    search_fields = ["name", "category__name"]
    ordering_fields = ["price", "created_at"]

    def perform_create(self, serializer):
        serializer.save()
        cache.clear() 

    def perform_update(self, serializer):
        serializer.save()
        cache.clear()

    def perform_destroy(self, instance):
        instance.delete()
        cache.clear()