"""Pytest configuration and fixtures."""

import pytest


@pytest.fixture
def sample_user_id() -> str:
    """Return a sample user ID for testing."""
    return "test_user_001"


# TODO: Add more fixtures as implementation progresses
# - sample_policy
# - sample_content_filter
# - sample_user
# - sample_session
