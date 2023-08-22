from django.urls import path
from . import views

app_name = 'e_app'

urlpatterns = [
    path('', views.home_view, name='home'),
    # Add more URLs as needed
]
