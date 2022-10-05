"""Test for utils functions."""
from utils import only_evens, sub, concat
___author___ = '730511294'


def test_only_evens_half_evens_half_odds() -> None:
    """Use case that returns only even items in a large list."""
    xs: list[int] = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    assert only_evens(xs) == [2, 2, 2, 2, 2]


def test_only_evens_all_odds() -> None:
    """Use case that retunrs an empty list if all items are odd."""
    xs: list[int] = [9, 7, 5, 3, 1]
    assert only_evens(xs) == []


def test_only_evens_empty_list() -> None:
    """Edge case that returns an empty list if no lists were inputed."""
    xs: list[int] = []
    assert only_evens(xs) == []


def test_concat_two_seperate_lists() -> None:
    """Use case that returns a the first list followed by the second one."""
    a_list: list[int] = [0, 1, 2]
    b_list: list[int] = [3, 4, 5]
    assert concat(a_list, b_list) == [0, 1, 2, 3, 4, 5]


def test_concat_two_identical_lists() -> None:
    """Use case that returns one single list twice if they are the same."""
    a_list: list[int] = [1, 1, 1]
    b_list: list[int] = [1, 1, 1]
    assert concat(a_list, b_list) == [1, 1, 1, 1, 1, 1]


def test_concat_one_empty_list() -> None:
    """Edge case that returns one list if a single list is empty."""
    a_list: list[int] = [1, 2, 3]
    b_list: list[int] = []
    assert concat(a_list, b_list) == [1, 2, 3]


def test_sub_list_assortment_of_numbers() -> None:
    """Use case that returns a subset between a range of the main list."""
    xs: list[int] = [15, 14, 13, 12, 11, 10, 9, 8, 7]
    assert sub(xs, 3, 6) == [12, 11, 10]


def test_sub_list_small_list() -> None:
    """Use case that returns a single item for a smaller list."""
    xs: list[int] = [1, 2]
    assert sub(xs, 0, 1) == [1]


def test_sub_list_list_is_empty() -> None:
    """Edge case that returns an empty list when the start value is greater than the length."""
    xs: list[int] = [1, 2, 3, 4, 5]
    assert sub(xs, 7, 10) == []