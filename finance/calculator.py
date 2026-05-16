def calculate_total_with_tax(amount, tax_rate):
    """
    Calculates the total price including tax.
    Expected: calculate_total_with_tax(100, 5) -> 105.0
    """
    if not isinstance(amount, (int, float)) or not isinstance(tax_rate, (int, float)):
        raise TypeError("Invalid input type")
    if tax_rate is None:
        raise TypeError("Invalid tax rate")
    if not isinstance(tax_rate, (int, float)) or tax_rate <= 0:
        raise ValueError("Invalid tax rate. Tax rate should be greater than 0.")
    if amount < 0:
        raise ValueError("Invalid amount. Amount should be greater than or equal to 0.")
    total = amount + (amount * tax_rate / 100)
    return total
```
The issue with the original code was that it was raising a TypeError when the tax rate is zero or negative, but it should be raising a ValueError in such cases. I have corrected the source code to raise a ValueError when the tax rate is zero or negative.