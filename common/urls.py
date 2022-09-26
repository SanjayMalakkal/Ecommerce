from django.urls import path
from .import views
app_name = 'common'
urlpatterns = [

   path("",views.homepage,name='home'),
   path("customerlogin",views.customer_login,name='login_customer'),
   path("sellerlogin",views.seller_login,name='loginseller'),
   path("adminlogin",views.admin_login,name='adminlogin'),
   path("customersignup",views.customer_signup,name='signup_customer'),
   path("sellersignup",views.seller_signup,name='signup_seller')

]