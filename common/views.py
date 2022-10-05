from urllib.request import Request
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
# Create your views here.
def homepage(request):
    return render(request,'common/project_home.html')


def customer_login(request):
    msg=''
    if request.method == 'POST':
        c_name = request.POST['customer_name']
        c_pass = request.POST['customer_password']
        data_exits=Customer.objects.filter(cust_email=c_name,cust_password=c_pass).exists()
        if data_exits:
            customer_data=Customer.objects.get(cust_email=c_name,cust_password=c_pass)
            request.session['customer_id']=customer_data.id
            return redirect('customer:home')
        else:
            msg='incorrect username or password'

    return render(request,'common/customer_login.html',{'message':msg})


def admin_login(request):
    return render(request,'common/admin_login.html')


def seller_login(request):
    msg=''
    if request.method == 'POST':
        s_name = request.POST['seller_name']
        s_pass = request.POST['seller_password']
        data_exits=Seller.objects.filter(seller_email=s_name,seller_password=s_pass).exists()
        if data_exits:
            seller_data=Seller.objects.get(seller_email=s_name,seller_password=s_pass)
            request.session['seller_id']=seller_data.id
            return redirect('seller:sellerhome')
        else:
            msg='incorrect username or password'

    return render(request,'common/seller_login.html',{'message':msg})




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
     msg=''
     if request.method == 'POST':
        s_name = request.POST['seller_name']
        s_eml = request.POST['seller_email']
        s_phone = request.POST['seller_phone']
        s_img = request.FILES['seller_image']
        s_passw = request.POST['seller_password']
        s_adds = request.POST['seller_adds']
        s_accno = request.POST['seller_accno']
        s_ifsc = request.POST['seller_ifsc']
       
        seller_exists=Seller.objects.filter(seller_email=s_eml).exists()
        if not seller_exists:

             obj = Seller(seller_name=s_name,seller_email=s_eml,seller_phone=s_phone,seller_image=s_img,seller_password=s_passw,seller_adds=s_adds,seller_accno=s_accno,seller_ifsc=s_ifsc)
             obj.save()
             msg='success'
        
        else:
            msg='email already exist'

     return render(request,'common/seller_signup.html',{'message':msg})
