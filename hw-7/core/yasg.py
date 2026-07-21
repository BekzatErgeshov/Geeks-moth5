from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation", 
        default_version=1,
        description="API documentations for the project",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


# smtp 

# google account 

# 2 аутентификация 

# создать приложение  