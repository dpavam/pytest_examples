# import pytest
from functions.convert_to_int import convert_to_int
# Implementing TDD

# Write the tests for a function that takes a number as a string, using commas
# to separate thousands and returns an integer

# Normal arugments:
# Try using 3 different cases, no comma, 1 comma, 2 commas


def test_no_comma():
    actual = convert_to_int("789")
    assert actual == 789, f"Expected: 789, instead got {actual}."


def test_one_comma():
    actual = convert_to_int("12,654")
    assert actual == 12654, f"Expected: 12654, instead got {actual}."


def test_two_commas():
    actual = convert_to_int("12,654,000")
    assert actual == 12654000, f"Expected: 12654000, instead got {actual}."


# Special arguments:
# Those that are missing a comma, a comma in the wrong place, and floats
# Should return None

def test_string_missing_comma():
    actual = convert_to_int("789456,123")
    assert actual is None, f"Expected: None, instead got {actual}"


def test_comma_wrong_place():
    actual = convert_to_int("12,65,654")
    assert actual is None, f"Expected: None, instead got {actual}"


def test_string_is_not_float():
    actual = convert_to_int("12,656.54")
    assert actual is None, f"Expected: None, instead got {actual}"
