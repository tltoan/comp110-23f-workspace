"""Ultility Function."""

__author__: str = "730676929"


def all(lst: list[int], num: int) -> bool:  
    """Returns a boolean value indicating whether all int in the list are equal to the given integer."""
    i: int = 0
    if len(lst) == 0:
        return False
    while i < len(lst):
        if lst[i] != num:
            return False  # if given integer does not equal all that is in the list, return false
        else:
            i += 1
    return True  # if given integer equal all that is in the list, return ture


def max(lst: list[int]) -> int:
    """Returns the largest integer given a list of integers."""
    if len(lst) == 0:
        raise ValueError("max() arg is an empty List")  # if list is emtpy, raise an error
    max_num = lst[0]  # 
    i = 1
    while i < len(lst):
        if lst[i] > max_num:
            max_num = lst[i]
        i += 1
    return max_num


def is_equal(lst1: list[int], lst2: list[int]) -> bool:
    """Given 2 lists, returns false if any integer at any index not equal eachother."""
    if len(lst1) != len(lst2):  # if list 1 does not equal list 2, print False
        return False
    i = 0
    while i < len(lst1):
        if lst1[i] != lst2[i]:
            return False
        i += 1
    return True  # if list 1 equal list 2, return true