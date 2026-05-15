"""
QualityEngine Test App — intentionally has bugs for demo purposes.
"""


def divide(a, b):
    # BUG: No zero-division check
    return a / b


def get_user(user_id, db):
    # SECURITY BUG: SQL injection vulnerability
    query = f"SELECT * FROM users WHERE id = {user_id}"
    return db.execute(query)


def calculate_discount(price, discount_percent):
    # BUG: No validation — negative discount or >100% possible
    discount = price * discount_percent / 100
    return price - discount


def process_items(items):
    # BUG: ZeroDivisionError on empty list
    total = 0
    for item in items:
        total += item["price"] * item["quantity"]
    return total / len(items)


def hash_password(password):
    # SECURITY BUG: MD5 is cryptographically broken
    import hashlib
    return hashlib.md5(password.encode()).hexdigest()


# SECURITY BUG: hardcoded secret in source code
SECRET_KEY = "hardcoded_secret_key_12345"
API_TOKEN  = "sk-prod-abc123xyz789"
