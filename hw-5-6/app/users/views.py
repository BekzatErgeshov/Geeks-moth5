from rest_framework import mixins, status, viewsets
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from app.users.models import User
from app.users.serializers import (
    LogoutSerializer,
    ProfileSerializer,
    RegisterSerializer
)

class RegisterViewSet(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet
):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def create(self, reqyest, *args, **kwargs):
        serialiser = self.get_serializer(data=reqyest.data)
        serialiser.is_valid(raise_exception=True)
        serialiser.save()
        return Response(
            {
                "message": "User created successfully"
            },
            status=status.HTTP_201_CREATED
        )

class LoginViewSet(
    viewsets.GenericViewSet
):

    serializer_class = TokenObtainPairSerializer
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(
            serializer.validated_data,
            status=status.HTTP_200_OK
        )

class LogoutViewSet(
    viewsets.GenericViewSet
):
    serializer_class = LogoutSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
                "message": "Вы успешно вышли из аккаунта"
            },
            status=status.HTTP_205_RESET_CONTENT
        )

class ProfileAPIView(RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user