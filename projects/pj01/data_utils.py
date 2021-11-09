"""Utility functions."""

__author__ = "730490857"

# Define your functions below
from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of csv into a 'table'."""
    result: list[dict[str, str]] = []

    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")

    # Prepare to read the data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)
    # Close the file when we are done, to free its resources.
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)

    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(table: dict[str, list[str]], n_rows: int) -> dict[str, list[str]]:
    """Produces a new column-based table that has the first N rows of data."""
    result: dict[str, list[str]] = {}

    for column in table:
        first_rows: list[str] = []
        i: int = 0
        if n_rows > len(table[column]):
            n_rows = len(table[column])
        while i < n_rows:
            first_rows.append(table[column][i])
            i += 1
        result[column] = first_rows

    return result


def select(table: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Produces a new column-based table with only specific columns from the orignal table."""
    result: dict[str, list[str]] = {}

    for column in names:
        result[column] = table[column]
        
    return result


def concat(table_1: dict[str, list[str]], table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combines two column-based table into one column-based table."""
    result: dict[str, list[str]] = {}

    for column in table_1:
        result[column] = table_1[column]
    for column in table_2:
        if column in result:
            result[column].extend(table_2[column])
        else:
            result[column] = table_2[column]

    return result


def count(xs: list[str]) -> dict[str, int]:
    """Counts the number of times a value appears in a list and associates the value with a key in a dictionary."""
    result: dict[str, int] = {}
    i: int = 0
    while i < len(xs):
        if xs[i] in result:
            result[xs[i]] += 1
        else:
            result[xs[i]] = 1
        i += 1

    return result