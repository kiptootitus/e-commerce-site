from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('view-cart/', views.CartView.as_view(), name='view-cart'),
    # Add more URLs as needed
]
