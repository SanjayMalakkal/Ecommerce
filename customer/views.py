from urllib.request import Request
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def cust_home(request):
    return render(request,'customer/customer_home.html')


def cust_update(request):
    return render(request,'customer/update_profile.html')


def order_history(request):
    return render(request,'customer/order_history.html')


def change_password(request):
    return render(request,'customer/change_password.html')



def product_det(request):
    return render(request,'customer/product_details.html')


def view_cart(request):
    return render(request,'customer/view_cart.html')

