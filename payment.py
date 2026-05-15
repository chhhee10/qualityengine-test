import os
import requests

def create_stripe_charge(amount_cents: int, source_token: str):
    """
    Creates a charge using the Stripe API.
    """
    stripe_key = os.environ.get("STRIPE_SECRET_KEY")
    
    response = requests.post(
        "https://api.stripe.com/v1/charges",
        auth=(stripe_key, ""),
        data={
            "amount": amount_cents,
            "currency": "usd",
            "source": source_token,
            "description": "Test charge"
        }
    )
    return response.json()
