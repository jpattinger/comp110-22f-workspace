"""First Example of Lists!"""
__author__ = '730511294'


def all(list: list[int], number: int) -> bool:
    """Boolean example that determines if every element in a list is the same integer."""
    i: int = 0
    if len(list) == 0:
        return False
    while i < len(list):
        if list[i] == number:
            i += 1  
        else:
            return False
    return True


def max(input: list[int]) -> int:
    """Example that returns the max integer in a list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0
    highest_number: int = input[0]
    while i < len(input):
        if input[i] > highest_number:
            highest_number = input[i]
        i += 1
    return highest_number


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Boolean example that sees if two lists are idetical to each other."""
    i: int = 0
    if len(list_1) != len(list_2):
        return False
    while i < len(list_1):
        if list_1[i] != list_2[i]:
            return False
        i += 1
    return True    