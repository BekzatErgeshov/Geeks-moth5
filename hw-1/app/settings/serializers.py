from rest_framework import serializers

from app.settings.models import Category, Product, ProductImage

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "name", "image"
        )

class ProductImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = (
            "id", "image"
        )

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializers(
        source="product_image",
        many=True,
        read_only=True
    )

    class Meta:
        model = Product
        fields = (
            "id", "name", "description","price",
            "created_at", "images"
        )


class CalculatorSerializer(serializers.Serializer):
    first_value = serializers.FloatField()
    second_value = serializers.FloatField()
    operator = serializers.ChoiceField(choices=("+", "-", "*", "/"))

    def validate(self, attrs):
        if attrs["operator"] == "/" and attrs["second_value"] == 0:
            raise serializers.ValidationError(
                {"second_value": "Cannot divide by zero."}
            )
        return attrs


class TemperatureSerializer(serializers.Serializer):
    temperature = serializers.FloatField(min_value=-10, max_value=40)
