def geraints_function(a, b):
    """
    Returns the absolute difference between a and b

        >>> geraints_function(7, 9)
        2
        >>> round(geraints_function(20.4, 3.1), 1)
        17.3
    """
    return max(b-a, a-b)