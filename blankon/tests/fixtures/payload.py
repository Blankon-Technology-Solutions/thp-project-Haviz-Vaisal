from datetime import datetime, timedelta

import pytest
from django.utils import timezone


@pytest.fixture
def login_payload():
    return {"username": "test_a@test.com", "password": "test1234"}


@pytest.fixture
def register_payload():
    return {
        "email": "test@test.com",
        "password": "test1234!@",
        "confirm_password": "test1234!@",
    }


@pytest.fixture
def create_todo_payload():
    return {"title": "Test", "description": "Test"}
