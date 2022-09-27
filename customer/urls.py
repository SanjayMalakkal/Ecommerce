from django.urls import path
from .import views
app_name = 'customer'
urlpatterns = [

   path("",views.cust_home,name='home'),
   path("updateprofile",views.cust_update,name='updateprofile'),
   path("orderhistory",views.order_history,name='orderhistory'),
   path("changepassword",views.change_password,name='changepassword'),
   path("productdetails",views.product_det,name='productdetails'),
   path("view_cart",views.view_cart,name='view_cart')

]