"""Test my zip function."""


__author__ = "730696929"

from lessons.zip import zip


def edge_case_empty_list():
    """Test zip function with empty input lists."""
    expected = zip([], [])
    assert expected == {}


def use_case_equal_value():
    """Test function with input lists of equal value."""
    result = zip(["apples", "oranges", "kiwis"], [3, 2, 1])
    expected = {"apples": 3, "oranges": 2, "kiwis": 1}
    assert result == expected


def use_case_different_lengths():
    """Test width inputs lists of different length."""
    expected = zip(["X", "Y"]), [10, 20, 30]
    assert expected == {}