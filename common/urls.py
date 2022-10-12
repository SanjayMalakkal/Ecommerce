from django.urls import path
from .import views
app_name = 'common'
urlpatterns = [

   path("",views.homepage,name='home'),
   path("customerlogin",views.customer_login,name='customerlogin'),
   path("sellerlogin",views.seller_login,name='sellerlogin'),
   path("adminlogin",views.admin_login,name='adminlogin'),
   path("customersignup",views.customer_signup,name='customersignup'),
   path("sellersignup",views.seller_signup,name='sellersignup'),
   path("email_check",views.check_email,name='check'),
   path("customer_email_check",views.cust_check_email,name='check')

]