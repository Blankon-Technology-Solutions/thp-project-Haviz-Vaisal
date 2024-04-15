from datetime import datetime
from http import HTTPStatus

import pytest
from django.urls import reverse

from todos.models import Todo


@pytest.mark.django_db
def test_update_todo_success(client, user_a, todo_url, create_todo_payload, todo):
    client.force_authenticate(user_a)
    response = client.patch(todo_url, data=create_todo_payload)
    assert response.status_code == HTTPStatus.OK

    event = Todo.objects.get(id=todo.id)
    for field, value in create_todo_payload.items():
        if field == "created_at":
            value = datetime.strptime(value, "%Y-%m-%d").date()

        assert getattr(event, field) == value


@pytest.mark.parametrize(
    "field, value, expected_error",
    [
        ("title", "", "This field may not be blank."),
        ("description", "", "This field may not be blank."),
    ],
)
@pytest.mark.django_db
def test_update_todo_failed(
    client,
    user_a,
    todo_url,
    create_todo_payload,
    field,
    value,
    expected_error,
):
    create_todo_payload[field] = value
    client.force_authenticate(user_a)
    response = client.patch(todo_url, create_todo_payload)
    assert expected_error in str(response.content)


@pytest.mark.django_db
def test_update_other_user_todo(
    client,
    user_b,
    todo_url,
    create_todo_payload,
):
    client.force_authenticate(user_b)
    response = client.patch(todo_url, create_todo_payload)
    assert response.status_code == HTTPStatus.NOT_FOUND


@pytest.mark.django_db
def test_update_todo_not_found(
    client,
    user_a,
):
    client.force_authenticate(user_a)
    response = client.delete(reverse("todos:todos-detail", kwargs={"pk": 12}))
    assert response.status_code == HTTPStatus.NOT_FOUND


@pytest.mark.django_db
def test_update_todo_unauthorized(
    client,
    todo_url,
    create_todo_payload,
):
    response = client.post(todo_url, create_todo_payload)
    assert response.status_code == HTTPStatus.UNAUTHORIZED
