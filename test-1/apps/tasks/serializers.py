from datetime import date

from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ('id', 'created_at')

    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError(
                "Название должно содержать минимум 5 символов."
            )
        return value

    def validate_description(self, value):
        if len(value) < 10:
            raise serializers.ValidationError(
                "Описание должно содержать минимум 10 символов."
            )
        return value

    def validate_priority(self, value):
        if value not in (1, 2, 3, 4, 5):
            raise serializers.ValidationError(
                "Приоритет может быть только от 1 до 5."
            )
        return value

    def validate_deadline(self, value):
        if value < date.today():
            raise serializers.ValidationError(
                "Дедлайн не может быть в прошлом."
            )
        return value


class TaskListSerializer(serializers.ModelSerializer):
    """Сериализатор для списка задач (только нужные поля)."""

    class Meta:
        model = Task
        fields = ('id', 'title', 'priority')
