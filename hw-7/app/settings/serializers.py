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
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all()
    )

    class Meta:
        model = Product
        fields = (
            "id", "name", "description","price",
            "created_at", "category", "images"
        )

    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Название продукта должно быть не менее 3 символов.")
        return value 

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Цена продукта должна быть положительным числом.")
        return value

    def validate_category(self, value):
        if not Category.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("Выбранная категория не существует.")
        return value

    def validate(self, attrs):
        name = attrs.get("name")
        description = attrs.get("description")

        if name and description:
            if name.lower() in description.lower():
                raise serializers.ValidationError(
                    "Описание продукта не должно содержать его название."
                )
        return attrs