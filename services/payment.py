def calculate_tax(amount, rate):
    """
    Calculate tax based on the given amount and rate.

    Args:
        amount (float): The amount to calculate tax for.
        rate (float): The tax rate.

    Returns:
        float: The calculated tax.

    Raises:
        TypeError: If amount or rate is not a number.
    """
    if not isinstance(amount, (int, float)) or not isinstance(rate, (int, float)):
        raise TypeError("Amount and rate must be numbers")
    return amount * rate  # Corrected the calculation to multiplication