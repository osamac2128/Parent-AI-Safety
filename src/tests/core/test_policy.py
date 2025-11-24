"""Tests for safety policy engine."""

import pytest

from parent_ai_safety.core.policy import SafetyLevel, SafetyPolicy, SafetyRule


class TestSafetyRule:
    """Tests for SafetyRule model."""

    def test_create_safety_rule(self) -> None:
        """Test creating a safety rule."""
        rule = SafetyRule(
            name="test_rule",
            description="Test rule description",
            enabled=True,
            priority=10,
        )
        assert rule.name == "test_rule"
        assert rule.enabled is True
        assert rule.priority == 10


class TestSafetyPolicy:
    """Tests for SafetyPolicy model."""

    def test_create_policy(self) -> None:
        """Test creating a safety policy."""
        policy = SafetyPolicy(name="test_policy", level=SafetyLevel.MODERATE)
        assert policy.name == "test_policy"
        assert policy.level == SafetyLevel.MODERATE
        assert len(policy.rules) == 0

    def test_validate_not_implemented(self) -> None:
        """Test that validate() raises NotImplementedError."""
        policy = SafetyPolicy(name="test", level=SafetyLevel.STRICT)
        with pytest.raises(NotImplementedError):
            policy.validate()

    def test_enforce_not_implemented(self) -> None:
        """Test that enforce() raises NotImplementedError."""
        policy = SafetyPolicy(name="test", level=SafetyLevel.STRICT)
        with pytest.raises(NotImplementedError):
            policy.enforce("test content")


# TODO: Add tests when implementation is complete
# - test_policy_validation
# - test_policy_enforcement
# - test_rule_conflicts
# - test_policy_merging
