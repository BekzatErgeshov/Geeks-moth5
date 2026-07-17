from django.urls import path
from rest_framework.routers import DefaultRouter

from app.users.views import (
    LoginViewSet,
    LogoutViewSet,
    ProfileAPIView,
    RegisterViewSet
)

router = DefaultRouter()

router.register("register", RegisterViewSet, basename="register")
router.register("login", LoginViewSet, basename="login")
router.register("logout", LogoutViewSet, basename="logout")

urlpatterns = [
    path("profile/", ProfileAPIView.as_view(), name="profile"),
]

urlpatterns += router.urls
