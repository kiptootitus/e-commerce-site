from django.urls import path
from . import views

app_name = 'payment'

urlpatterns = [
    path('make-payment/', views.PaymentView.as_view(), name='make-payment'),
    # Add more
]