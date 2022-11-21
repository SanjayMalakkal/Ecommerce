from urllib.request import Request
from django.shortcuts import redirect, render
from django.http import HttpResponse,JsonResponse
from .decorator import auth_customer
from common.models import Customer
from seller.models import Product
from .models import *
# Create your views here.
def cust_home(request):
    customer_data = Customer.objects.get(id = request.session['customer_id'])
    return render(request,'customer/customer_home.html',{'customer' : customer_data})

@auth_customer
def cust_update(request):
    return render(request,'customer/update_profile.html')

@auth_customer
def order_history(request):
    return render(request,'customer/order_history.html')

@auth_customer
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


@auth_customer
def product_det(request,pid):

    if 'customer_id' in request.session:
        product = Product.objects.get(id=pid)
        
    else:
        return redirect('common:customerlogin')
    return render(request,'customer/product_details.html',{'product' : product})

@auth_customer
def view_cart(request):
    cart_item = Cart.objects.filter(customer=request.session['customer_id'])
    return render(request,'customer/view_cart.html',{'cart_item':cart_item})

def logout(request):
    del request.session['customer_id']
    request.session.flush()
    return redirect('common:home')

@auth_customer
def add_to_cart(request,pid):


    if 'customer_id' in request.session:
        product = Product.objects.get(id=pid)
        customer = Customer.objects.get(id = request.session['customer_id'])
        product_exist = Cart.objects.filter(product = pid,customer=request.session['customer_id']).exists()
        if not product_exist:
            cart = Cart(customer=customer,product=product)
            cart.save()
            if request.session['cart_msg']:
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


@auth_customer
def remove_item(request,pid):

    product = Product.objects.get(id=pid)
    customer = Customer.objects.get(id = request.session['customer_id'])
    items = Cart.objects.get(product = pid,customer=request.session['customer_id'])
    items.delete()
    return redirect('customer:viewcart')


def order_product(request,pid):
    customer = request.session['cust_id']
    product = Product.objects.get(id=pid)
    order_date = datetime.datetime.now().time()
    delivery_status = 'order placed'
    address = request.POST['address']
    payment_id = request.razorpay_payment_id
    order_id = request.razorpay_order_id
    payment_type = 'online'
    payment_amount = request.POST['total']


    




          
    