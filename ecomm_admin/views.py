from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def view_seller(request):
    return render(request,'ecomm_admin/view_seller.html')