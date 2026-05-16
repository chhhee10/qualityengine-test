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
        raise TypeError("Invalid tax rate. Tax rate should be greater than 0.")
    if amount < 0:
        raise TypeError("Invalid amount. Amount should be greater than or equal to 0.")
    total = amount + (amount * tax_rate / 100)
    return total
```
The issue in the original code was that the test cases were correct, but the source code was not properly handling the case when the tax rate is zero or negative. The source code has been modified to raise a TypeError in such cases.