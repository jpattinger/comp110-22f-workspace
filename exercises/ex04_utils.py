"""First Example of Lists"""
__author__ = '730511294'

def all(list: list[int], number: int) -> bool:
    i: int = 0
    while i < len(list):
        if list[i] == number:
            i += 1  
        else:
            return False
    return True



def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0
    highest_number: int = 0
    while i < len(input):
        if input[i] > highest_number:
            highest_number = input[i]
            i += 1
        else:
            i += 1
    return highest_number



def is_equal(list_1: int, list_2: int) -> bool:
    i: int = 0
    if list_1 != list_2:
        return False
    while list_1 == list_2:
        if list_1[i] == list_2[i]:
            i += 1
        return True