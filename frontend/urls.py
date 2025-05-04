from django.urls import path

from frontend.views import home, auth_login, auth_logout, register, cart

urlpatterns = [
    path('', home, name="home"),
    path('login', auth_login, name='login'),
    path('logout/', auth_logout, name='logout'),
    path('register', register, name='register'),
    path('cart', cart)
]