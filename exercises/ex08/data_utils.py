"""Dictionary related utility functions."""
from csv import DictReader
__author__ = "730511294"


def read_csv_rows(a: str) -> list[dict[str, str]]:
    """Converts a CSV into lists of rows."""
    result: list[dict[str, str]] = []
    file_handle = open(a, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(b: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of every value in a column."""
    result: list[str] = []
    for row in b:
        place: str = row[column]
        result.append(place)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Converts a row oriented table to a column-orientated table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(c: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Create a new column with only the first parameter of a column."""
    result: dict[str, list[str]] = {}
    for key in c:
        if n > len(c[key]):
            return c
        answer: list[str] = []
        i: int = 0
        while i < n:
            answer.append(c[key][i])
            i += 1
        result[key] = answer
    return result


def select(a: dict[str, list[str]], list_1: list[str]) -> dict[str, list[str]]:
    """Creates a table with specific columns."""
    result: dict[str, list[str]] = {}
    for key in list_1:
        result[key] = a[key]
    return result


def concat(a: dict[str, list[str]], b: dict[str, list[str]]) -> dict[str, list[str]]:
    """Creates a new table through the combination of two tables."""
    result: dict[str, list[str]] = {}
    for key in a:
        result[key] = a[key]
    for key in b:
        if key in result:
            i: int = 0
            while i < len(b[key]):
                result[key].append(b[key][i])
                i += 1
        else:
            result[key] = b[key]
    return result


def count(a: list[str]) -> dict[str, int]:
    """Will make a dict when given a list of special keys."""
    result: dict[str, int] = {}
    for key in a:
        if key in result:
            result[key] += 1
        else:
            result[key] = 1
    return result