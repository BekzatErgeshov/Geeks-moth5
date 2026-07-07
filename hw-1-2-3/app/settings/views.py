from rest_framework.generics import ListAPIView, CreateAPIView,\
RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.core.cache import cache

from app.settings.models import Category, Product
from app.settings.serializers import (
    CalculatorSerializer,
    CategorySerializers,
    ProductSerializer,
    TemperatureSerializer,
)

CATEGORY_LIST_CACHE_KEY = 'category_list'
CATEGORY_LIST_CACHE_TTL = 60 * 15  # 15 минут

class CategoryAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

    def list(self, request, *args, **kwargs):
        cached_data = cache.get(CATEGORY_LIST_CACHE_KEY)
        if cached_data is not None:
            return Response(cached_data)

        response = super().list(request, *args, **kwargs)
        cache.set(CATEGORY_LIST_CACHE_KEY, response.data, CATEGORY_LIST_CACHE_TTL)
        return response

class ProductListAPIView(ListAPIView):
    queryset = Product.objects.prefetch_related(
        "product_image"
        ).select_related("category")
    serializer_class = ProductSerializer
    @method_decorator(cache_page(60 * 5))  # Cache for 15 minutes
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class ProductCreateAPIView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
@method_decorator(cache_page(60 * 5), name='get')  # Cache for 15 minutes
class ProductRetrieveAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductUpdateAPIView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDestroyAPIView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def perform_destroy(self, instance):
        instance.delete()
        cache.clear()

class CalculatorAPIView(APIView):
    def post(self, request):
        serializer = CalculatorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        first_value = serializer.validated_data["first_value"]
        second_value = serializer.validated_data["second_value"]
        operator = serializer.validated_data["operator"]

        if operator == "+":
            result = first_value + second_value
        elif operator == "-":
            result = first_value - second_value
        elif operator == "*":
            result = first_value * second_value
        else:
            result = first_value / second_value

        return Response(
            {
                "first_value": first_value,
                "second_value": second_value,
                "operator": operator,
                "result": result,
            }
        )


class TemperatureAPIView(APIView):
    def post(self, request):
        serializer = TemperatureSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        temperature = serializer.validated_data["temperature"]

        if temperature <= 10:
            temperature_type = "низкая температура"
        elif temperature <= 25:
            temperature_type = "нормальная температура"
        else:
            temperature_type = "очень жарко"

        return Response(
            {
                "temperature": temperature,
                "type": temperature_type,
            }
        )
