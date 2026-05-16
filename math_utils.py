def broken_add(a, b):
    """Adds two numbers"""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both inputs must be numbers")
    if isinstance(a, list) or isinstance(b, list):
        raise TypeError("Both inputs must be numbers, not lists")
    return a + b