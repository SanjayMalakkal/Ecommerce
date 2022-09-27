from urllib.request import Request
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def seller_home(request):
    return render(request,'seller/seller_home.html')


def product_catelog(request):
    return render(request,'seller/product_catelog.html')


def update_stock(request):
    return render(request,'seller/update_stock.html')


def change_password(request):
    return render(request,'seller/change_password.html')



def profile(request):
    return render(request,'seller/profile.html')


def add_product(request):
    return render(request,'seller/my_order.html')


