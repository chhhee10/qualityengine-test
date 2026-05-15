"""Helper utilities for demo merge."""
import re
from typing import Optional

def clamp(value: float, low: float, high: float) -> float:
    if low > high:
        raise ValueError("low must be <= high")
    return max(low, min(high, value))

def slugify(text: str) -> str:
    if not text:
        return ""
    text = text.strip().lower()
    return re.sub(r"[^a-z0-9]+", "-", text).strip("-")
