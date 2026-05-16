def calculate_total_with_tax(amount, tax_rate):
    """
    Calculates the total price including tax.
    Expected: calculate_total_with_tax(100, 5) -> 105.0
    """
    if not isinstance(amount, (int, float)) or not isinstance(tax_rate, (int, float)):
        raise TypeError("Invalid input type")
    if tax_rate is None:
        raise TypeError("Invalid tax rate")
    total = amount + (amount * tax_rate / 100)
    return total