"""Edge and Use cases to test three dictionary fucntions!"""
__author__ = '730511294'

import pytest
from exercises.ex07.dictionary import invert, count, favorite_colors

def test_inverts_a_single_key_in_dictionary() -> None:
    """Takes a single key in a dictionary."""
    answer: dict[str, str] = {'cat': 'apple'}
    assert invert(answer) == {'apple': 'cat'}


def test_inverts_a_complicated_dictionary_of_keys() -> None:
    """Switches multiple keys in a complex dictionary."""
    answer: dict[str, str] = {'a': '1', 'b': '2', 'c': '3', 'd': '4'}
    assert invert(answer) == {'1': 'a', '2': 'b', '3': 'c', '4': 'd'}


def test_inverts_an_empty_dictionary() -> None:
    """Returns a empty dictionary."""
    answer: dict[str, str] = {}
    assert invert(answer) == {}


def test_favorite_colors_with_most_frequency() -> None:
    """Returns the color that appears the most."""
    answer: dict[str, str] = {"jackson": "blue", "max": "blue", "nikita": "yellow"}
    assert favorite_colors(answer) == "blue"


def test_favorite_colors_with_no_frequency() -> None:
    """Returns the first color when none appear the most frequently."""
    answer: dict[str, str] = {"jackson": "blue", "myles": "green"}
    assert favorite_colors(answer) == "blue"


def test_favorite_colors_no_dictionary() -> None:
    """Returns an empty dictionary when none is presented."""
    answer: dict[str, str] = {}
    assert favorite_colors(answer) == ""


def test_count_simple_dictionary() -> None:
    """Returns a dictionary with a single most frequent item."""
    answer: list[str] = ['a', 'a', 'a', 'b', 'b', 'c']
    assert count(answer) == {'a': 3, 'b': 2, 'c': 1}


def test_count_dictionary_withi_no_greatest_value() -> None:
    """Returns the first value when the dictionary has no greatest value."""
    answer: list[str] = ['a', 'b', 'c']
    assert count(answer) == {'a': 1, 'b': 1, 'c': 1}


def test_count_return_empty_dictionary() -> None:
    """Returns an empty dictionary when no list is presented."""
    answer: list[str] = []
    assert count(answer) == {}


