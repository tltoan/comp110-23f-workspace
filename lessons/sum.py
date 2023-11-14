"""Summing the elements of a list using different loops."""


__author__ = 730676929


def w_sum(vals: list[float]) -> float:
    """Takes as input a list of floats and returns the sum of all elements."""
    sum = 0
    i = 0
    while i < len(vals):
        sum += int(vals[i])
        i += 1
    return sum


def f_sum(vals: list[float]) -> float:
    """Calculating the sum of all elements in vals but uses a for ... in ... loop."""
    sum = 0
    for val in vals:
        sum += int(val)
    return sum


def f_range_sum(vals: list[float]) -> float:
    """Calculating the sum of all elements in vals but uses a for ... in range(...) loop."""
    sum = 0
    for i in range(len(vals)):
        sum += int(vals[i])
    return sum
