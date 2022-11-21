from urllib.request import Request
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .decorator import auth_admin
from common.models import Seller
from common.models import Customer
from common.models import Admin
from django.core.mail import send_mail
from .models import *
# Create your views here.

def homepage(request):
    admin_data = Admin.objects.get(id = request.session['admin_id'])
    return render(request,'ecomm_admin/ecomm_home.html',{'admin_data' : admin_data})

    
@auth_admin
def view_seller(request):
    return render(request,'ecomm_admin/view_seller.html')

@auth_admin
def approve_seller(request):
    return render(request,'ecomm_admin/approve_seller.html')

@auth_admin
def view_customer(request):
    return render(request,'ecomm_admin/view_customer.html')

@auth_admin
def load_Sellers(request):
    sellers = Seller.objects.filter(seller_status='pending')
    data = [{'id': seller.id, 'name': seller.seller_name, 'email': seller.seller_email,
             'address': seller.seller_adds, 'phone': seller.seller_phone,'image': seller.seller_image.url} for seller in sellers]
             
    print(data)
    return JsonResponse({'data': data})

@auth_admin
def approved_Sellers(request):
    sellers = Seller.objects.filter(seller_status='approved')
    data = [{'id': seller.id, 'name': seller.seller_name, 'email': seller.seller_email,
             'address': seller.seller_adds, 'phone': seller.seller_phone, 'image': seller.seller_image.url} for seller in sellers]
             
    print(data)
    return JsonResponse({'data': data})

@auth_admin
def customer_available(request):
    customers = Customer.objects.all()
    data = [{'id': customer.id, 'name': customer.cust_name, 'email': customer.cust_email,
              'phone': customer.cust_phone,'image': customer.cust_image.url} for customer in customers]
             
    print(data)
    return JsonResponse({'data': data})

@auth_admin
def delete_seller(request):
    id = request.POST['id']
    seller = Seller.objects.get(id=id)
    seller.delete()
    return JsonResponse({'status': 'seller deleted'})

@auth_admin
def seller_approval(request):
    id = request.POST['id']
    seller = Seller.objects.get(id=id)
    seller.seller_status='approved'
    seller.save()
    send_mail(
    'Approved',
    'Hi {{seller.seller_name}} we are pleased to inform you that user request has been approved.',
    'sanjayproject222@gmail.com',
    [seller.seller_email],
    fail_silently=False,
)
    return JsonResponse({'status': 'seller approved'})


def logout(request):
    del request.session['admin_id']
    request.session.flush()
    return redirect('common:adminlogin')

