import pytest
import os
import numpy as np
from functions.advanced_operations import txt_to_array

# Examples of using fixtures to create setup for tests.
# Setup a fixutre
# Note, if within a Test class, pass the self arg.


@pytest.fixture
def new_file():
    file = "test_input.txt"
    with open(file, "w") as f:
        f.write("1\n 2\n 3\n 4\n 5")
    yield file
    os.remove(file)

# Test the function

# Checks the returned value is a numpy array.


def test_txt_to_array_type(new_file):
    actual = txt_to_array(new_file)
    assert isinstance(actual, np.ndarray)


# tmpdir & fixture chaining
# Avoids need for manual teardown of path, file needs manual removal.

@pytest.fixture
def tmpdir_file(tmpdir):
    file = tmpdir.join("tmpdir_input.txt")
    with open(file, "w") as f:
        f.write("1\n 2\n 3\n 4\n 5")
    yield file
    os.remove(file)

# Test the content of the array


def test_txt_to_array_content(tmpdir_file):
    actual = txt_to_array(tmpdir_file)
    expected = np.array([1, 2, 3, 4, 5])
    assert np.array_equal(actual, expected)
