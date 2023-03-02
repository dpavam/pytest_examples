def suma(*args):
    """Take any number of arguments and adds them."""
    return sum(args)


def double(*args):
    """Take any number of arguments and multiplies them them."""
    return tuple([arg*2 for arg in args])


def say_hi():
    """Print hello world."""
    return "Hello World"
