from rest_framework import mixins, status, viewsets
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from app.users.models import User
from app.users.serializers import RegisterSerializer
from app.users.utils import send_registration_email

class RegisterViewSet(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet
):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def create(self, reqyest, *args, **kwargs):
        serialiser = self.get_serializer(data=reqyest.data)
        serialiser.is_valid(raise_exception=True)
        user = serialiser.save()
        send_registration_email(user)
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