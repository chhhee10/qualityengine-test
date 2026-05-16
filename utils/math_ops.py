def add(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        if a is None or b is None:
            return None
        elif isinstance(a, str) and a == '' and isinstance(b, (int, float)):
            return b
        elif isinstance(b, str) and b == '' and isinstance(a, (int, float)):
            return a
        else:
            raise TypeError("Both inputs must be numbers")
    return a + b

def multiply(a, b):
    """Multiply two numbers safely."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        if a is None or b is None:
            return None
        elif isinstance(a, str) and a == '' and isinstance(b, (int, float)):
            return 0
        elif isinstance(b, str) and b == '' and isinstance(a, (int, float)):
            return 0
        else:
            raise TypeError("Both inputs must be numbers")
    return a * b