from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.shortcuts import render, redirect

from backend.models import Cart


# Create your views here.
def home(request):
    return render(request, 'frontend/home.html')

def auth_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=email, password=password)

        if user is not None:
            # Login the user
            login(request, user)
            return redirect('home')  # Redirect to a success page
        else:
            messages.error(request, 'Invalid email or password')
    return render(request, 'frontend/auth/login.html')

def auth_logout(request):
    logout(request)  # Log out the user
    return redirect('home')  # Redirect to the login page or home page

def cart(request):
    context = {
        'cart': Cart.objects.all()
    }
    return render(request, "frontend/cart.html", context)
