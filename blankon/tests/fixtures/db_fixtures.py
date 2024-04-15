import pytest

from accounts.models import User
from todos.models import Todo


@pytest.fixture(autouse=True)
def user_a():
    """Initialize test user."""
    return User.objects.create_user(
        "test_a@test.com",
        "test1234",
    )


@pytest.fixture(autouse=True)
def user_b():
    """Initialize test user."""
    return User.objects.create_user(
        "test_b@test.com",
        "test1234",
    )


@pytest.fixture
def todo(user_a):
    return Todo.objects.create(
        title="test",
        description="description",
        creator=user_a,
    )
