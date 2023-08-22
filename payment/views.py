from django.views.generic import TemplateView

class PaymentView(TemplateView):
    template_name = 'payment/payment.html'
