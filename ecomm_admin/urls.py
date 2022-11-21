from django.urls import path
from .import views
app_name = 'ecomm_admin'
urlpatterns = [
   path("",views.homepage,name='home'),
   path("viewseller",views.view_seller,name='viewseller'),
   path("approveseller",views.approve_seller,name='approveseller'),
   path("viewcustomer",views.view_customer,name='viewcustomer'),
   path("loadseller",views.load_Sellers,name='loadseller'),
   path("logout",views.logout,name='logout'),
   path("approvedsellers",views.approved_Sellers,name='approvedsellers'),
   path("customers",views.customer_available,name='customers'),
   path("deleteseller",views.delete_seller,name='seller'),
   path("sellerapproval",views.seller_approval,name='sellerapproval')

]