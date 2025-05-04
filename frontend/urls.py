from django.urls import path

from frontend.views import home, auth_login, auth_logout, cart

urlpatterns = [
    path('', home, name="home"),
    path('login', auth_login, name='login'),
    path('logout/', auth_logout, name='logout'),
    path('cart', cart)
]