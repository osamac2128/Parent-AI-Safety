"""Tests for content filtering."""

import pytest

from parent_ai_safety.core.filter import (
    ContentCategory,
    ContentFilter,
    FilterAction,
    FilterRule,
)


class TestFilterRule:
    """Tests for FilterRule model."""

    def test_create_filter_rule(self) -> None:
        """Test creating a filter rule."""
        rule = FilterRule(
            name="profanity_filter",
            category=ContentCategory.PROFANITY,
            action=FilterAction.BLOCK,
            keywords={"bad_word1", "bad_word2"},
        )
        assert rule.name == "profanity_filter"
        assert rule.category == ContentCategory.PROFANITY
        assert len(rule.keywords) == 2


class TestContentFilter:
    """Tests for ContentFilter."""

    def test_create_filter(self) -> None:
        """Test creating a content filter."""
        filter_obj = ContentFilter()
        assert len(filter_obj.rules) == 0

    def test_filter_not_implemented(self) -> None:
        """Test that filter() raises NotImplementedError."""
        filter_obj = ContentFilter()
        with pytest.raises(NotImplementedError):
            filter_obj.filter("test content")


# TODO: Add tests when implementation is complete
# - test_keyword_filtering
# - test_pattern_matching
# - test_content_sanitization
# - test_multiple_rules
