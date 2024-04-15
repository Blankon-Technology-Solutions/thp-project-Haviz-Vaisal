from http import HTTPStatus

import pytest


@pytest.mark.django_db
def test_retrieve_todo_success(
    client,
    user_a,
    todo_url,
):
    client.force_authenticate(user_a)
    response = client.get(todo_url)
    assert response.status_code == HTTPStatus.OK


@pytest.mark.django_db
def test_retrieve_other_user_todo(
    client,
    user_b,
    todo_url,
):
    client.force_authenticate(user_b)
    response = client.get(todo_url)
    assert response.status_code == HTTPStatus.NOT_FOUND


@pytest.mark.django_db
def test_retrieve_todo_unauthorized(
    client,
    todo_url,
):
    response = client.get(todo_url)
    assert response.status_code == HTTPStatus.UNAUTHORIZED
