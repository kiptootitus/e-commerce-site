from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('orders/', include('orders.urls', namespace='orders')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('products/', include('products.urls', namespace='products')),
    path('', include('e_app.urls', namespace='e_app')),
    path('payment/', include('payment.urls', namespace='payment')),
    # Other project-level URLs
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
