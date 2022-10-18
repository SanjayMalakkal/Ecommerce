from math import prod
from urllib.request import Request
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from common.models import Seller
# Create your views here.
def seller_home(request):
    seller_data =  Seller.objects.get(id = request.session['seller_id'])
 
    return render(request,'seller/seller_home.html',{'seller':seller_data})


def product_catelog(request):
    return render(request,'seller/product_catelog.html')


def update_stock(request):
    return render(request,'seller/update_stock.html')


def change_password(request):
    msg = ""
    if request.method == 'POST':
        
        c_password = request.POST['current_password']
        n_password = request.POST['new_password']
        conf_password = request.POST['confirm_password']
        seller_data =  Seller.objects.get(id = request.session['seller_id'])
        if c_password == seller_data.seller_password:
            if n_password == conf_password:
                seller_data.seller_password = n_password
                seller_data.save()
                msg = "Password changed succesfully"
            else:
                msg = "Password does not match"
        else:
            msg = "Incorrect Passsword"


    return render(request,'seller/change_password.html',{'msg':msg})



def profile(request):
    return render(request,'seller/profile.html')


def add_product(request):
    
    if request.method == 'POST':
        pro_number = request.POST['product_number']
        pro_name = request.POST['product_name']
        pro_description = request.POST['product_description']
        pro_price = request.POST['product_price']
        pro_stock = request.POST['product_stock']
        pro_image = request.FILES['product_image']
        product = Product(p_name = pro_name,p_number=pro_number,p_description=pro_description,p_price=pro_price,
        p_stock=pro_stock,p_image=pro_image,seller_id = request.session['seller_id'] )
        product.save()
        msg = 'product added'
        return render(request,'seller/my_order.html',{'msg':msg})
    return render(request,'seller/my_order.html')


def logout(request):
    del request.session['seller_id']
    request.session.flush()
    return redirect('common:home')

