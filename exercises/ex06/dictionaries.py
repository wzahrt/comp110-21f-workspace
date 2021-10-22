"""Practice with dictionaries."""

__author__ = "730490857"

# Define your functions below


def invert(x: dict[str, str]) -> dict[str, str]:
    """Inverts the keys with the values in a dictionary."""
    result: dict[str, str] = {}
    k: int = 0
    for key in x:
        for r in x:
            if x[key] == x[r]:
                k += 1
    k = k - len(x)
    if k > 0:
        raise KeyError
    for key in x:
        result[x[key]] = key
    return result


def favorite_color(x: dict[str, str]) -> str:
    """Looks are the values in a dictionary and returns the most common one."""
    most_common: str = ""
    j: int = 0
    for key in x:
        k: int = 0
        for b in x:
            if x[key] == x[b]:
                k += 1
        if k >= j:
            most_common = x[key]
            j = k + 1
    return most_common


def count(xs: list[str]) -> dict[str, int]:
    """Counts the amount of items in a list and assigns the to keys in a dictionary. The value of the dictionary is how many times it appears."""
    result: dict[str, int] = {}
    i: int = 0
    while i < len(xs):
        if xs[i] in result:
            result[xs[i]] += 1
        else:
            result[xs[i]] = 1
        i += 1
    return result
