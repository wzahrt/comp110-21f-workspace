"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
# from exercises.ex05.utils import only_evens, sub, concat
from exercises.ex05.utils import only_evens, sub, concat


__author__ = "123456789"


def test_utils_empty() -> None:
    assert only_evens([]) == []


def test_utils_two_numbers() -> None:
    assert only_evens([1, 2]) == [2]


def test_utils_zero_included() -> None:
    assert only_evens([0, 1, 2, 3, 5, 0, 4]) == [2, 4]


def test_utils_multiple_evens() -> None:
    assert only_evens([2, 2, 2, 4, 4, 4, 3, 6]) == [2, 2, 2, 4, 4, 4, 6]


def test_utils_negative_end_index() -> None:
    assert sub([1, 2, 3], 1, -1) == []


def test_utils_empty_list() -> None:
    assert sub([], -1, 3) == []


def test_utils_list() -> None:
    assert sub([1, 2, 3, 4], 1, 3) == [2, 3]


def test_utils_negative_start() -> None:
    assert sub([1, 2, 3, 4], -1, 3) == [1, 2, 3]


def test_utils_larger_end_index() -> None:
    assert sub([1, 2, 3, 4], 1, 5) == [2, 3, 4]


def test_utils_random_list() -> None:
    assert sub([3, 4, 8, 21, 5], -60, 4) == [3, 4, 8, 21]


def test_utils_first_use() -> None:
    assert concat([1, 2, 3], [1, 2, 3]) == [1, 2, 3, 1, 2, 3]


def test_utils_one_empty_list() -> None:
    assert concat([1, 2, 3], []) == [1, 2, 3]


def test_utils_two_empty_lists() -> None:
    assert concat([], []) == []


def test_utils_one_big_one_small() -> None:
    assert concat([1, 2, 3, 4, 5, 6, 7, 8, 9], [1]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]