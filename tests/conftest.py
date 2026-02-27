""" @file conftest.py
    @author Sean Duffie
    @brief Discovered by Pytest and Defines "fixtures" (reusable test data)
"""
import pytest
from project.models import UserProfile

@pytest.fixture
def sample_user():
    """Provides a valid user model for testing."""
    return {
        "username": "test_user",
        "email": "test@example.com"
    }
