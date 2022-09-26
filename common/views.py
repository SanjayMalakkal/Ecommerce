from urllib.request import Request
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def homepage(request):
    return render(request,'common/project_home.html')


def customer_login(request):
    return render(request,'common/customer_login.html')


def admin_login(request):
    return render(request,'common/admin_login.html')


def seller_login(request):
    return render(request,'common/seller_login.html')


def customer_signup(request):
    msg=''
    if request.method == 'POST':
        c_name = request.POST['cust_name']
        c_eml = request.POST['cust_email']
        c_phone = request.POST['cust_phone']
        c_img = request.FILES['cust_file']
        c_passw = request.POST['cust_password']
       
        customer_exists=Customer.objects.filter(cust_email=c_eml).exists()
        if not customer_exists:

             obj = Customer(cust_name=c_name,cust_email=c_eml,cust_phone=c_phone,cust_image=c_img,cust_password=c_passw)
             obj.save()
             msg='success'
        
        else:
            msg='email already exist'

    return render(request,'common/customer_signup.html',{'message':msg})
    


def seller_signup(request):
    return render(request,'common/seller_signup.html')
