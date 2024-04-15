from django.urls import path, include
from rest_framework import routers


from todos.views import TodoViewSet


router = routers.DefaultRouter()
router.register(r"", TodoViewSet, basename="todos")

urlpatterns = [
    path("", include(router.urls)),
]
