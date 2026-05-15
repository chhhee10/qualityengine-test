"""
math_utils.py
Provides secure and robust mathematical utilities for the application.
"""
from typing import List, Union

def calculate_average(numbers: List[Union[int, float]]) -> float:
    """
    Calculates the average of a list of numbers.
    
    Args:
        numbers: A list of integers or floats.
        
    Returns:
        The average as a float.
        
    Raises:
        ValueError: If the input list is empty.
        TypeError: If the input is not a list.
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of numbers")
        
    if not numbers:
        raise ValueError("Cannot calculate average of an empty list")
        
    return sum(numbers) / len(numbers)

def apply_discount(price: float, discount_percentage: float) -> float:
    """
    Applies a discount to a given price securely.
    
    Args:
        price: The original price.
        discount_percentage: The discount to apply (0 to 100).
        
    Returns:
        The final price after discount.
        
    Raises:
        ValueError: If price is negative or discount is out of bounds.
    """
    if price < 0:
        raise ValueError("Price cannot be negative")
        
    if not (0 <= discount_percentage <= 100):
        raise ValueError("Discount must be between 0 and 100")
        
    discount_amount = price * (discount_percentage / 100)
    return round(price - discount_amount, 2)
