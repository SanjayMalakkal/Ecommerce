from urllib.request import Request
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def homepage(request):
    return render(request,'ecomm_admin/ecomm_home.html')

def view_seller(request):
    return render(request,'ecomm_admin/view_seller.html')


def approve_seller(request):
    return render(request,'ecomm_admin/approve_seller.html')


def view_customer(request):
    return render(request,'ecomm_admin/view_customer.html')

