from django.views.generic import TemplateView
from .models import Cart

class CartView(TemplateView):
    template_name = 'cart/cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add code to fetch cart data and add it to the context
        return context
