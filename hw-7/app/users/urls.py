from rest_framework.routers import DefaultRouter
from app.users.views import RegisterViewSet, LoginViewSet

router = DefaultRouter()

router.register("register", RegisterViewSet, basename="register")
router.register("login", LoginViewSet, basename="login")

urlpatterns = router.urls