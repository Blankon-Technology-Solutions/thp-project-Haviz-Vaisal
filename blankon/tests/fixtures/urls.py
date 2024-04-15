import pytest
from django.urls import reverse


@pytest.fixture
def login_url():
    return reverse("accounts:token_obtain_pair")


@pytest.fixture
def register_url():
    return reverse("accounts:auth_register")


@pytest.fixture
def create_todo_url():
    return reverse("todos:todos-list")


@pytest.fixture
def todo_url(todo):
    return reverse(
        "todos:todos-detail",
        kwargs={"pk": todo.id},
    )
