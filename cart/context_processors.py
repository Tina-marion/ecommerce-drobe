"""Context processors for the `cart` app.

This provides a minimal `cart_count` processor expected by the project's
`TEMPLATES` setting. It reads a session-based cart (a dict mapping product
IDs to item dicts containing a `quantity` key) and returns the total
quantity. The implementation is defensive and falls back to zero if the
session data isn't present or malformed.
"""
from typing import Dict

from django.http import HttpRequest


def cart_count(request: HttpRequest) -> Dict[str, int]:
    """Return {'cart_count': <int>} for templates.

    Expected session shape (example):
        request.session['cart'] = {
            '1': {'quantity': 2, ...},
            '42': {'quantity': 1, ...},
        }
    """
    cart = request.session.get('cart', {})
    total = 0
    try:
        if isinstance(cart, dict):
            total = sum(int(item.get('quantity', 0)) for item in cart.values() if isinstance(item, dict))
    except Exception:
        total = 0
    return {"cart_count": total}
