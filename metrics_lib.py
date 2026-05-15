"""Small metrics helpers — clean, validated code."""
from __future__ import annotations
from typing import List


def mean(values: List[float]) -> float:
    if not values:
        raise ValueError("values must not be empty")
    return sum(values) / len(values)


def median(values: List[float]) -> float:
    if not values:
        raise ValueError("values must not be empty")
    sorted_vals = sorted(values)
    n = len(sorted_vals)
    mid = n // 2
    if n % 2:
        return sorted_vals[mid]
    return (sorted_vals[mid - 1] + sorted_vals[mid]) / 2


def normalize(score: float, low: float, high: float) -> float:
    if high <= low:
        raise ValueError("high must be greater than low")
    if not (low <= score <= high):
        raise ValueError("score out of range")
    return (score - low) / (high - low)
