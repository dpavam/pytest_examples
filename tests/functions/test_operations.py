import pytest
from functions.operations import suma, double, say_hi

# Using test classes, one per function

# Test class for suma, note cammel case, begins with word Test,
# pass object as arg, pass self to each test.


class TestSuma(object):

    # Example of using multiple assert statements.
    # Simple test checking the function adds.
    # Tests a normal argument
    def test_suma_does_add(self):
        # Save the actual test
        actual = suma(4, 5)
        # Expected answer
        expected = 9
        # Error message for adding.
        message_add = f'The suma(4,5) returned {actual} instead of {expected}.'
        # Error message for type
        message_type = f"The type for suma(4,5) returned \
                        {type(actual)} instead of int or float."
        # Perform the test, if it fails, the message is displayed
        # Test the function adds correctly.
        assert actual == expected, message_add
        # Test the result is numerical.
        assert isinstance(actual, (int, float)), message_type

    # Example of using the pytest.approx method.
    # Test that the function can add floats
    # Tests a normal argument
    def test_suma_floats(self):
        actual = suma(3.5+6.5)
        expected = 10
        message = f'The suma(3.5+6.5) returned {actual} instead of {expected}.'
        assert actual == pytest.approx(expected), message

    # Unit tests for exceptions
    # Test that the function does not accept string values
    # Tests a bad argument
    def test_suma_string_in_input(self):
        # The test passes if there is a type error
        with pytest.raises(TypeError):
            suma("4"+5)
        # Matching the error message is also an option using as exc_info.
        # assert exc_info.match('can only concatenate str (not "int") to str')

# Test class for double


class TestDouble(object):

    # Normal arg test for double.
    def test_double_doubles(self):
        actual = double(4, 5)
        expected = (8, 10)
        assert actual == expected, f"Expected {expected}, instead got {actual}"

# Example of skipping and expected failure
# Test class for say hi


class TestSayHi(object):

    # Skipping
    @pytest.mark.skipif(True, reason='Function for noobs only.')
    def test_should_not_run(self):
        assert say_hi() != "Goodbye World"

    # Xfailing
    @pytest.mark.xfail(reason="Because it's only hello world")
    def test_should_x_fail(self):
        assert say_hi() == "Goodbye World"
