def calculate_total_with_tax(amount, tax_rate):
    """
    Calculates the total price including tax.
    Expected: calculate_total_with_tax(100, 5) -> 105.0
    """
    # BUG 1: Logic error (forgot to divide rate by 100)
    # BUG 2: Syntax error (trailing comma causing a tuple return)
    total = amount + (amount * tax_rate)
    return total , 
