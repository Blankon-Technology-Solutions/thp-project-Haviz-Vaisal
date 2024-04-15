from http import HTTPStatus

import pytest


@pytest.mark.django_db
def test_register_success(client, register_url, register_payload):
    response = client.post(register_url, data=register_payload)
    assert response.status_code == HTTPStatus.CREATED
    assert "id" in response.json()


@pytest.mark.parametrize(
    "field, value",
    [
        ("password", "invalid"),
        ("confirm_password", "invalid"),
        ("email", "invalid-email"),
    ],
)
@pytest.mark.django_db
def test_register_failed(
    client,
    register_url,
    register_payload,
    field,
    value,
):
    register_payload[field] = value
    response = client.post(register_url, data=register_payload)
    assert response.status_code == HTTPStatus.BAD_REQUEST
