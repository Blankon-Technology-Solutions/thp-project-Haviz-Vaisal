from django.urls import re_path

from todos.cunsomers import TodoConsumer

websocket_urlpatterns = [
    re_path(r"ws/todos/$", TodoConsumer.as_asgi()),
]
