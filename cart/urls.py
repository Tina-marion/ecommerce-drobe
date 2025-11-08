from django.urls import path
from django.views.generic import TemplateView

# Minimal URL patterns for the cart app. A placeholder view/template is
# provided so templates can reverse 'cart_detail' until the real cart
# implementation exists.
urlpatterns = [
    path('', TemplateView.as_view(template_name='cart/detail.html'), name='cart_detail'),
]
