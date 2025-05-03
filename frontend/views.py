from django.http import JsonResponse
from django.shortcuts import render

from backend.models import Cart


# Create your views here.
def home(request):
    return render(request, 'frontend/home.html')

def cart(request):
    context = {
        'cart': Cart.objects.all()
    }
    return render(request, "frontend/cart.html", context)
