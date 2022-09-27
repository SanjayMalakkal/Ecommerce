from django.urls import path
from .import views
urlpatterns = [
   path("viewseller",views.view_seller,name='viewseller'),
   path("approveseller",views.approve_seller,name='approveseller'),
   path("viewcustomer",views.view_customer,name='viewcustomer')

]