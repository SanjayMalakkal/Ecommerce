from django.urls import path
from .import views
app_name = 'ecomm_admin'
urlpatterns = [
   path("",views.homepage,name='home'),
   path("viewseller",views.view_seller,name='viewseller'),
   path("approveseller",views.approve_seller,name='approveseller'),
   path("viewcustomer",views.view_customer,name='viewcustomer')

]