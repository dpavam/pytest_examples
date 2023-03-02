import numpy as np


def txt_to_array(file):
    """Convert the content of a text file into an array."""
    with open(file, "r") as f:
        lines = f.readlines()
        return np.array([int(line.strip()) for line in lines])


# print(txt_to_list('input.txt'))
