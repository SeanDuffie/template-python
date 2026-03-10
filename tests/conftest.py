## @file conftest.py
#  @author Sean Duffie
#  @brief Discovered by Pytest and Defines "fixtures" (reusable test data)

import pytest
# from project.models import UserProfile


@pytest.fixture
def sample_user():
    """Provides a valid user model for testing."""
    test_user_mapping = {"username": "test_user", "email": "test@example.com"}
    # test_user = UserProfile(username="test_user", email="test@example.com")

    return test_user_mapping
