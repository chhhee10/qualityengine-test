"""Pricing helpers — amounts are in CENTS (integers)."""
from __future__ import annotations

def cents_to_dollars(cents: int) -> float:
    if cents < 0:
        raise ValueError("cents cannot be negative")
    return round(cents / 100.0, 2)

def dollars_to_cents(dollars: float) -> int:
    if dollars < 0:
        raise ValueError("dollars cannot be negative")
    return int(round(dollars * 100))

def apply_tax_cents(subtotal_cents: int, rate_percent: float) -> int:
    if subtotal_cents < 0:
        raise ValueError("subtotal cannot be negative")
    if not (0 <= rate_percent <= 100):
        raise ValueError("rate must be 0-100")
    return int(round(subtotal_cents * rate_percent / 100.0))
