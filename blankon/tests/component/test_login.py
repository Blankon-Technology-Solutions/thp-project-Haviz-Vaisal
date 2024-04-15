from http import HTTPStatus

import pytest


@pytest.mark.django_db
def test_login_success(client, login_url, login_payload):
    response = client.post(login_url, data=login_payload)
    assert response.status_code == HTTPStatus.OK


@pytest.mark.django_db
def test_login_failed(client, login_url, login_payload):
    login_payload["password"] = "invalid"  # noqa S105
    response = client.post(login_url, data=login_payload)
    assert response.status_code == HTTPStatus.UNAUTHORIZED
