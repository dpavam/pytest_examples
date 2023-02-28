# Written using TTD.

def convert_to_int(string):
    sep_parts_list = string.split(',')

    for i in range(len(sep_parts_list)):
        # Write an if statement for checking missing commas
        if len(sep_parts_list[i]) > 3:
            return None

        # Write the if statement for incorrectly placed commas
        if i != 0 and len(sep_parts_list[i]) != 3:
            return None

    # Join the parts
    comma_filtered_str = "".join(sep_parts_list)

    # Try to return as an int
    try:
        return int(comma_filtered_str)
    # Fill in with a ValueError
    except ValueError:
        return None
