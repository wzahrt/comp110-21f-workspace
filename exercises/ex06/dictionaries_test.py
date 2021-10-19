"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex06.dictionaries import invert, favorite_color, count
import pytest
__author__ = "730490857"


def test_dictionaries_one_key() -> None:
    """Inverts one key."""
    assert invert({"a": "b"}) == {"b": "a"}


def test_dictionaries_multiple_key() -> None:
    """Inverts multiple keys."""
    assert invert({"a": "b", "c": "d", "e": "f"}) == {"b": "a", "d": "c", "f": "e"}


def test_dictionaries_multiple_values() -> None:
    """Raises KeyError if there are multiple of the same key being inverted."""
    with pytest.raises(KeyError):
        my_dictionary = {"a": "b", "c": "b"}
        invert(my_dictionary)


def test_dictionaries_favorite_color() -> None:
    """Given a dictionary the function will give back a string with the most repeated value."""
    assert favorite_color({"Jack": "blue", "Ted": "red", "Tim": "blue"}) == "blue"


def test_dictionaries_favorite_color_no_multiples() -> None:
    """Given a dictionary with no repeated values the output is the first value given."""
    assert favorite_color({"Jack": "blue", "Ted": "red", "Tim": "green", "Aaron": "black"}) == "blue"


def test_dictionaries_favorite_color_later_multiples() -> None:
    """Given a dictionary with tied amounts of favorite colors, the function gives back the first of the multiple favorite colors stated."""
    assert favorite_color({"Jack": "blue", "Ted": "red", "Tim": "green", "Aaron": "black", "Will": "red", "Sam": "blue"}) == "blue"


def test_dictionaries_no_dictionary() -> None:
    """When there is nothing in the dictionary an emptry string is the output."""
    assert favorite_color({}) == ""


def test_count_normal_use() -> None:
    """Counts the number of variable in a list. Number of times it appears is the value in the dictionary."""
    assert count(["a", "b", "c", "a"]) == {"a": 2, "b": 1, "c": 1}


def test_count_normal_use_again() -> None:
    """Counts the number of variable in a list. Number of times it appears is the value in the dictionary."""
    assert count(["hello", "no", "bye", "bye", "bye", "no"]) == {"hello": 1, "no": 2, "bye": 3}


def test_count_normal_empty_list() -> None:
    """Counts the number of variable in a list. Number of times it appears is the value in the dictionary."""
    assert count([]) == {}