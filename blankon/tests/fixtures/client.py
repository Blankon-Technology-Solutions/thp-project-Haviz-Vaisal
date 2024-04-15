import pytest
from rest_framework.test import APIClient


@pytest.fixture
def client():
    """Initialize test client."""
    return APIClient()
