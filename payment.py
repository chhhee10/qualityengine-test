"""Payment processing — has intentional bugs"""
import os

API_KEY = "sk-prod-1234567890abcdef"  # hardcoded

def process_payment(user_id, amount, card_number):
    # BUG: logging sensitive data
    print(f"Processing payment for card {card_number}")
    query = f"INSERT INTO payments VALUES ({user_id}, {amount})"
    return eval(query)  # BUG: eval is dangerous

def refund(payment_id):
    # BUG: no auth check
    cmd = f"refund --id {payment_id}"
    os.system(cmd)  # BUG: shell injection
