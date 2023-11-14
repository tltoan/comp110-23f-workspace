"""Combining two lists into a dictionary."""

__author__: 730696929


def zip(strings: list[str], integers: list[int]) -> dict[str, int]:
    """Creates a dictionary where keys are items from the 'strings' list and values are corresponding items from the 'integers' list."""
    if len(strings) != len(integers):
        return {}  # Return an empty dictionary if lists are of different lengths
    
    zipped_dict: dict[str, int] = {}  # Initialize an empty dictionary to store the result
    for i in range(len(strings)):
        zipped_dict[strings[i]] = integers[i]  # Assign each string from 'strings' to corresponding integer from 'integers'
    
    return zipped_dict