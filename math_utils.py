def add_numbers(a: int, b: int) -> int:
    """Adds two numbers"""
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both inputs must be integers")
    if isinstance(a, list) or isinstance(b, list):
        raise TypeError("Both inputs must be integers, not lists")
    return a + b