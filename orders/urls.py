from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('order-list/', views.OrderListView.as_view(), name='order-list'),
    path('order-detail/<int:pk>/', views.OrderDetailView.as_view(), name='order-detail'),
    # Add more URLs as needed
]
