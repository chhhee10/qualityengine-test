"""
Safe utility functions for the application.
All functions include proper input validation and error handling.
"""
from __future__ import annotations
import re
import logging
from typing import Optional

logger = logging.getLogger(__name__)


def safe_divide(a: float, b: float) -> Optional[float]:
    """
    Divide two numbers safely.
    Returns None if division by zero is attempted.

    >>> safe_divide(10, 2)
    5.0
    >>> safe_divide(5, 0) is None
    True
    """
    if b == 0:
        logger.warning("Division by zero attempted: %s / %s", a, b)
        return None
    return a / b


def validate_email(email: str) -> bool:
    """
    Validate an email address format.

    >>> validate_email("user@example.com")
    True
    >>> validate_email("not-an-email")
    False
    """
    if not isinstance(email, str) or not email:
        return False
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


def calculate_discount(price: float, discount_percent: float) -> float:
    """
    Calculate discounted price with full input validation.

    Args:
        price: Original price (must be >= 0)
        discount_percent: Discount percentage (must be 0-100)

    Returns:
        Discounted price

    Raises:
        ValueError: If inputs are invalid
    """
    if price < 0:
        raise ValueError(f"Price cannot be negative: {price}")
    if not (0 <= discount_percent <= 100):
        raise ValueError(f"Discount must be 0-100, got: {discount_percent}")

    discount = price * discount_percent / 100
    return round(price - discount, 2)


def process_items(items: list) -> dict:
    """
    Process a list of items and return summary statistics.
    Handles empty lists gracefully.

    Args:
        items: List of dicts with 'price' and 'quantity' keys

    Returns:
        Dict with total, average, count keys
    """
    if not items:
        return {"total": 0.0, "average": 0.0, "count": 0}

    total = sum(
        item["price"] * item["quantity"]
        for item in items
        if "price" in item and "quantity" in item
    )
    count = len(items)
    return {
        "total": round(total, 2),
        "average": round(total / count, 2),
        "count": count,
    }


def hash_password(password: str) -> str:
    """
    Hash a password using PBKDF2-SHA256 with random salt (secure).

    >>> len(hash_password("mysecret")) > 0
    True
    """
    import hashlib
    import os
    if not password:
        raise ValueError("Password cannot be empty")
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 100_000)
    return salt.hex() + ":" + key.hex()
