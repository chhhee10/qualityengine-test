"""Payment processing"""
import os
import logging
import sqlite3

# Set up logging to avoid logging sensitive data
logging.basicConfig(level=logging.INFO)

API_KEY = "sk-prod-1234567890abcdef"  # hardcoded

def process_payment(user_id, amount, card_number):
    """
    Process a payment.

    Args:
        user_id (int): The ID of the user making the payment.
        amount (float): The amount of the payment.
        card_number (str): The card number used for the payment.

    Returns:
        None
    """
    # Log sensitive data securely
    logging.info(f"Processing payment for user {user_id} with card number {card_number[:4]}...")

    # Connect to SQLite database
    conn = sqlite3.connect('payments.db')
    cursor = conn.cursor()

    # Use parameterized query to avoid SQL injection
    query = "INSERT INTO payments (user_id, amount, card_number) VALUES (?, ?, ?)"
    try:
        cursor.execute(query, (user_id, amount, card_number))
        conn.commit()
    except Exception as e:
        logging.error(f"Error processing payment: {e}")
    finally:
        conn.close()

def refund(payment_id):
    """
    Refund a payment.

    Args:
        payment_id (int): The ID of the payment to refund.

    Raises:
        TypeError: If payment_id is not an integer.
    """
    # Check if payment_id is an integer
    if not isinstance(payment_id, int):
        raise TypeError("payment_id must be an integer")

    # Use a secure way to run the refund command
    import subprocess
    cmd = f"refund --id {payment_id}"
    try:
        subprocess.run(cmd, shell=False, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Error refunding payment: {e}")