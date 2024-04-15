from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from todos.models import Todo
from todos.serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            # queryset just for schema generation metadata
            return Todo.objects.none()

        queryset = super().get_queryset()
        return queryset.filter(creator=self.request.user)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context
