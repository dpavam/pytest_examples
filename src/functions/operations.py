def suma(*args):
    """Takes any number of arguments separated by a comma and adds them
    """
    return sum(args)

def double(*args):
    """Takes any number of arguments separated by a comma and multiplies them them
    """
    return tuple([arg*2 for arg in args])

def say_hi():
    """Prints hello world"""
    return "Hello World"