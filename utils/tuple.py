def add(a, b):
    """Returns tuple with elements of both added together"""
    return tuple(z[0] + z[1] for z in zip(a, b))
