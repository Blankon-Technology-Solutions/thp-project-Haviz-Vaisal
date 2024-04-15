from http import HTTPStatus

import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_create_todo_success(
    client,
    user_a,
    create_todo_url,
    create_todo_payload,
):
    client.force_authenticate(user_a)
    response = client.post(create_todo_url, data=create_todo_payload)
    assert response.status_code == HTTPStatus.CREATED


@pytest.mark.parametrize(
    "field, value, expected_error",
    [
        ("title", "", "This field may not be blank."),
        ("description", "", "This field may not be blank."),
    ],
)
@pytest.mark.django_db
def test_create_todo_failed(
    client,
    user_a,
    create_todo_url,
    create_todo_payload,
    field,
    value,
    expected_error,
):
    create_todo_payload[field] = value
    client.force_authenticate(user_a)
    response = client.post(create_todo_url, data=create_todo_payload)
    assert expected_error in str(response.content)


@pytest.mark.django_db
def test_create_todo_unauthorized(
    client,
    create_todo_url,
    create_todo_payload,
):
    response = client.post(create_todo_url, data=create_todo_payload)
    assert response.status_code == HTTPStatus.UNAUTHORIZED
