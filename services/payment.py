def calculate_tax(amount, rate):
    # Fix: using multiplication instead of addition
    if not isinstance(amount, (int, float)) or not isinstance(rate, (int, float)):
        raise TypeError("Invalid input type")
    return amount * rate