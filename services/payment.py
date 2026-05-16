def calculate_tax(amount, rate):
    # Fix: added checks for empty and zero inputs
    if not isinstance(amount, (int, float)) or not isinstance(rate, (int, float)):
        raise TypeError("Invalid input type")
    if amount == 0 or rate == 0:
        raise TypeError("Amount and rate cannot be zero")
    return amount * rate