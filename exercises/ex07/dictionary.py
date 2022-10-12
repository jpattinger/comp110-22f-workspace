"""Exercise to showcase dictionary functions!"""
__author__ = '730511294'


from matplotlib.backend_bases import key_press_handler


def invert(inverted: dict[str, str]) -> dict[str, str]:
    """Given a dictionary, the fucntion inverts the keys and values."""
    answer: dict[str, str] = {}
    for key in inverted:
        if inverted[key] in answer:
            raise KeyError("Duplicate keys present.")
        else:
            answer[inverted[key]] = key
    return answer


def favorite_colors(a: dict[str, str]) -> str:
    """GIven a dictionary, will return the value that repeats the most frequently."""
    answer: str = ""
    frequency: dict[str, int] = {}
    frequency_1: int = 0
    for key in a:
        if a[key] in frequency:
            frequency[a[key]] += 1
        else:
            frequency[a[key]] = 1
    for key in frequency:
        if frequency_1 < frequency[key]:
            frequency_1 = frequency[key]
            answer = key
    return answer

def count(b: list[str]) -> dict[str, int]:
    answer: dict[str, int] = dict()
    for key in b:
        if key in answer:
            answer[key] += 1
        else:
            answer[key] = 1
    return answer