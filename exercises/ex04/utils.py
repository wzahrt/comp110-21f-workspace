"""List utility functions."""

__author__ = "730490857"

# TODO: Implement your functions here.


def all(haystack: list[int], needle: int) -> bool:
    """Return true if the needle is found in the haystack."""
    i: int = 0
    while i < len(haystack):
        item: int = haystack[i]
        if item == needle:
            return True
        i += 1

    return False
        

def is_equal(x: list[int], y: list[int]) -> bool:
    i: int = 0
    if len(x) != len(y):
        return False
    while i < len(x):
        if x[i] != y[i]:
            return False
        i += 1

    return True


def max(x: list[int]) -> int:
    if len(x) == 0:
        raise ValueError("max() arg is an empty list")
    i: int = 0
    k: int = 0
    while i < len(x) - 1:
        if x[i] < x[i + 1]:
            k = x[i + 1]
        else:
            k = x[i]
        i += 1
    return k
