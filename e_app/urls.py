from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'e_app'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
