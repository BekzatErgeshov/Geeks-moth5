from rest_framework import serializers
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken

from app.users.models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True
    )

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "phone",
            "password"
        )

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField(
        write_only=True
    )

    def validate_refresh(self, value):
        try:
            self.token = RefreshToken(value)
        except TokenError:
            raise serializers.ValidationError(
                "Refresh токен недействителен или уже истёк."
            )
        return value

    def save(self, **kwargs):
        self.token.blacklist()

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "phone",
            "first_name",
            "last_name",
            "date_joined"
        )
        read_only_fields = (
            "id",
            "username",
            "date_joined"
        )