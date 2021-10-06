"""List utility functions part 2."""

__author__ = "730490857"

# Define your functions below


def only_evens(x: list[int]) -> list[int]:
    """Returns a list of only even numbers."""
    i: int = 0
    even_list: list[int] = []
    while i < len(x):
        if x[i] == 0:
            i += 1
        elif x[i] % 2 == 0:
            even_list.append(x[i])
            i += 1
        elif x[i] % 2 == 1:
            i += 1
    return even_list


def sub(x: list[int], a: int, b: int) -> list[int]:
    """A list which returns the subset of a given list between the specified start index and the end index -1."""
    xs: list[int] = []
    if b <= 0:
        return xs
    if a > b:
        return xs
    if len(x) == 0:
        return xs
    if a < 0:
        a = 0
    if b > len(x):
        b = len(x)
    while a < b:
        xs.append(x[a])
        a += 1
    return xs


def concat(xs: list[int], ys: list[int]) -> list[int]:
    """Creates a mega-list that has all of the elements of the first list followed by all of th elements of the second."""
    zs: list[int] = []
    i: int = 0
    while i < len(xs):
        zs.append(xs[i])
        i += 1
    i = 0
    while i < len(ys):
        zs.append(ys[i])
        i += 1
    return zs