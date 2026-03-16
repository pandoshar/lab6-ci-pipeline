"""Tests for utils module."""
from src.utils import is_even, is_positive


def test_is_even():
    """Test is_even function."""
    assert is_even(2) is True
    assert is_even(3) is False
    assert is_even(0) is True


def test_is_positive():
    """Test is_positive function."""
    assert is_positive(5) is True
    assert is_positive(-5) is False
    assert is_positive(0) is False
