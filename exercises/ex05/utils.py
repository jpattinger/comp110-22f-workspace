"""Further examples of List with a directory!"""

___author___ = '730511294'

def only_evens(a_list: list[int]) -> list[int]:
    """A function that returns only the evens integers in a list."""
    i: int = 0
    only_evens_result: list[int] = list()
    while i < len(a_list):
        if a_list[i] % 2 == 0:
            only_evens_result.append(a_list[i])
        i += 1
    return only_evens_result
    
def concat(a_list: list[int], b_list: list[int]) -> list[int]:
    """A function that takes two lists and combines them, returning the first followed by the second."""
    concat_result: list[int] = list()
    i: int = 0
    while i < len(a_list):
        concat_result.append(a_list[i])
        i += 1
    i = 0
    while i < len(b_list):
        concat_result.append(b_list[i])
        i += 1
    return concat_result

def sub(a_list: list[int], min: int, max:int) -> list[int]:
    """A fucntion that will return the values in a list between two endpoints."""
    sub_result: list[int] = list()
    if min < 0:
        min = 0
    if max > len(a_list):
        end = len(a_list)
    if len(a_list) == 0 or max <= 0 or min >= len(a_list):
        return []
    while min < max:
        sub_result.append(a_list[min])
        min += 1
    return sub_result