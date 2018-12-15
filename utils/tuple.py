def add(a, b):
    """Returns tuple with elements of both added together"""
    return tuple(z[0] + z[1] for z in zip(a, b))

def around(origin):
    """All tuple locations that are directly next to some origin"""

    # List all the direction 'vectors'
    around = [(0,-1), (-1,0), (1,0), (0,1)]

    # Add these to the position to get a list of neighbours
    return [add(origin, dir) for dir in around]
