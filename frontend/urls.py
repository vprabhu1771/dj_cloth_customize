from django.urls import path

from frontend.views import home, cart

urlpatterns = [
    path('', home),
    path('cart', cart)
]