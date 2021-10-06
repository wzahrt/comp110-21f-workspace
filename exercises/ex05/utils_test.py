"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
# from exercises.ex05.utils import only_evens, sub, concat
from exercises.ex05.utils import only_evens, sub, concat


__author__ = "123456789"


def test_utils_empty() -> None:
    """Tests an empty list."""
    assert only_evens([]) == []


def test_utils_two_numbers() -> None:
    """Tests a list of two numbers."""
    assert only_evens([1, 2]) == [2]


def test_utils_zero_included() -> None:
    """Tests a list of numbers including 0."""
    assert only_evens([0, 1, 2, 3, 5, 0, 4]) == [2, 4]


def test_utils_multiple_evens() -> None:
    """Tests a list with multiple even numbers."""
    assert only_evens([2, 2, 2, 4, 4, 4, 3, 6]) == [2, 2, 2, 4, 4, 4, 6]


def test_utils_negative_end_index() -> None:
    """Tests a list with a negative end index."""
    assert sub([1, 2, 3], 1, -1) == []


def test_utils_empty_list() -> None:
    """Tests an empty list."""
    assert sub([], -1, 3) == []


def test_utils_list() -> None:
    """Tests a regular list with normal idexes."""
    assert sub([1, 2, 3, 4], 1, 3) == [2, 3]


def test_utils_negative_start() -> None:
    """Tests a list with a negative start index."""
    assert sub([1, 2, 3, 4], -1, 3) == [1, 2, 3]


def test_utils_larger_end_index() -> None:
    """Tests a list with an end index larger than the length of the list."""
    assert sub([1, 2, 3, 4], 1, 5) == [2, 3, 4]


def test_utils_random_list() -> None:
    """Tests a list with a massive negative start idex."""
    assert sub([3, 4, 8, 21, 5], -60, 4) == [3, 4, 8, 21]


def test_utils_first_use() -> None:
    """Tests a normal list with another normal list."""
    assert concat([1, 2, 3], [1, 2, 3]) == [1, 2, 3, 1, 2, 3]


def test_utils_one_empty_list() -> None:
    """Tests a list with an empty list."""
    assert concat([1, 2, 3], []) == [1, 2, 3]


def test_utils_two_empty_lists() -> None:
    """Tests two empty lists."""
    assert concat([], []) == []


def test_utils_one_big_one_small() -> None:
    """Tests a big list with a small one."""
    assert concat([1, 2, 3, 4, 5, 6, 7, 8, 9], [1]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]