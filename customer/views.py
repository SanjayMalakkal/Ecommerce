from urllib.request import Request
from django.shortcuts import render
from django.http import HttpResponse

from common.models import Customer
from .models import *
# Create your views here.
def cust_home(request):
    customer_data = Customer.objects.get(id = request.session['customer_id'])
    return render(request,'customer/customer_home.html',{'customer' : customer_data})


def cust_update(request):
    return render(request,'customer/update_profile.html')


def order_history(request):
    return render(request,'customer/order_history.html')


def change_password(request):
    msg = ""
    if request.method == 'POST':
        
        cur_password = request.POST['current_password']
        new_password = request.POST['new_password']
        conf_password = request.POST['confirm_password']
        customer_data =  Customer.objects.get(id = request.session['customer_id'])
        if cur_password == customer_data.cust_password:
            if new_password == conf_password:
                customer_data.cust_password = new_password
                customer_data.save()
                msg = "Password changed succesfully"
            else:
                msg = "Password does not match"
        else:
            msg = "Incorrect Passsword"

    return render(request,'customer/change_password.html',{'msg':msg})



def product_det(request):
    return render(request,'customer/product_details.html')


def view_cart(request):
    return render(request,'customer/view_cart.html')

