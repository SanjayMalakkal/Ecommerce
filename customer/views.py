from urllib.request import Request
from django.shortcuts import redirect, render
from django.http import HttpResponse,JsonResponse

from common.models import Customer
from seller.models import Product
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
                Customer.objects.filter(id = request.session['customer_id']).update(cust_password=new_password)
                msg = "Password changed succesfully"
            else:
                msg = "Password does not match"
        else:
            msg = "Incorrect Passsword"

    return render(request,'customer/change_password.html',{'msg':msg})



def product_det(request,pid):

    if 'customer_id' in request.session:
        product = Product.objects.get(id=pid)
        
    else:
        return redirect('common:customerlogin')
    return render(request,'customer/product_details.html',{'product' : product})


def view_cart(request):
    cart_item = Cart.objects.filter(customer=request.session['customer_id'])
    return render(request,'customer/view_cart.html',{'cart_item':cart_item})

def logout(request):
    del request.session['customer_id']
    request.session.flush()
    return redirect('common:home')


def add_to_cart(request,pid):

    msg = ''
    if 'customer_id' in request.session:
        product = Product.objects.get(id=pid)
        customer = Customer.objects.get(id = request.session['customer_id'])
        product_exist = Cart.objects.filter(product = pid).exists()
        if not product_exist:
            cart = Cart(customer=customer,product=product)
            cart.save()
            del request.session['cart_msg']
            return redirect('common:home')
        else:
            request.session['cart_msg'] = 'already in cart'
            return redirect('common:home')
    else:
        return redirect('common:customerlogin')  


          

def total_price(request):

    qty = request.POST['qty']
    price = request.POST['price']
    total = int(qty) * float(price)
    print(total)
    return JsonResponse({'total':total})

          
    