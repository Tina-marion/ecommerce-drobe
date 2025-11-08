"""Context processors for the `cart` app.

This provides a minimal `cart_count` processor expected by the project's
`TEMPLATES` setting. It reads a session-based cart (a dict mapping product
IDs to item dicts containing a `quantity` key) and returns the total
quantity. The implementation is defensive and falls back to zero if the
session data isn't present or malformed.
"""
from typing import Dict

from django.http import HttpRequest
from django.urls import reverse

# Import Product lazily to avoid import-time cycles in some settings
def _get_product_model():
    try:
        from products.models import Product
        return Product
    except Exception:
        return None


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


def cart_preview(request: HttpRequest) -> Dict[str, object]:
    """Return a small preview of cart items for the navbar.

    Returns {'cart_items': [ {id, name, quantity, price, image, url}, ... ]}
    Limits to first 3 items to keep templates lightweight.
    """
    cart = request.session.get('cart', {})
    Product = _get_product_model()
    items = []
    try:
        if isinstance(cart, dict) and Product is not None:
            # cart keys are product IDs as strings
            ids = [int(pid) for pid in list(cart.keys())[:10] if str(pid).isdigit()]
            products = {p.id: p for p in Product.objects.filter(id__in=ids)}
            for pid_str in list(cart.keys())[:3]:
                try:
                    pid = int(pid_str)
                except Exception:
                    continue
                item_data = cart.get(pid_str, {})
                product = products.get(pid)
                if not product:
                    continue
                items.append({
                    'id': product.id,
                    'name': product.name,
                    'quantity': int(item_data.get('quantity', 0)),
                    'price': str(product.price),
                    'image': getattr(product.image, 'url', ''),
                    'url': reverse('product_detail', kwargs={'pk': product.pk}),
                })
    except Exception:
        items = []
    return {'cart_items': items}
