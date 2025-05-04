from django.urls import path

from frontend.views import home, auth_login, cart

urlpatterns = [
    path('', home, name="home"),
    path('login', auth_login, name='login'),
    path('cart', cart)
]