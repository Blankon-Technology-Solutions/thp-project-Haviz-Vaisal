from django.urls import path, include, re_path
from django.conf import settings
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from todos.views import index

schema_view = get_schema_view(
    openapi.Info(
        title="Todo's API",
        default_version="v1",
        description="Rest API Documentation for Todo App",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("api/accounts/", include("accounts.urls")),
    path("api/todos/", include("todos.urls")),
    path("", index),
]

if settings.ENABLE_SWAGGER:
    urlpatterns += [
        re_path(
            r"^api/swagger(?P<format>\.json|\.yaml)$",
            schema_view.without_ui(cache_timeout=0),
            name="schema-json",
        ),
        re_path(
            r"^api/swagger/$",
            schema_view.with_ui("swagger", cache_timeout=0),
            name="schema-swagger-ui",
        ),
    ]
