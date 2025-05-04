from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.shortcuts import render, redirect

from django.contrib.auth.hashers import make_password

from backend.models import Cart, CustomerUser, Gender


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

def register(request):
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        gender = request.POST.get('gender', Gender.MALE)
        password = request.POST.get('password', '')
        confirm_password = request.POST.get('confirmPassword', '')

        # Validate required fields
        if not email or not phone or not password or not confirm_password:
            messages.error(request, 'All fields are required.')
        elif password != confirm_password:
            messages.error(request, 'Passwords do not match.')
        elif CustomerUser.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
        elif CustomerUser.objects.filter(phone=phone).exists():
            messages.error(request, 'Phone number already exists.')
        else:
            # Create the user
            CustomerUser.objects.create(
                email=email,
                phone=phone,
                gender=gender,
                password=make_password(password),
            )
            messages.success(request, 'Account created successfully. Please login.')
            return redirect('login')  # Change 'login' to your actual login URL name

    return render(request, 'frontend/auth/register.html')

def cart(request):
    context = {
        'cart': Cart.objects.all()
    }
    return render(request, "frontend/cart.html", context)
