from django.urls import path
from .import views
app_name = 'customer'
urlpatterns = [

   path("",views.cust_home,name='home'),
   path("updateprofile",views.cust_update,name='updateprofile'),
   path("orderhistory",views.order_history,name='orderhistory'),
   path("changepassword",views.change_password,name='changepassword'),
   path("productdetails/<int:pid>",views.product_det,name='productdetails'),
   path("viewcart",views.view_cart,name='viewcart'),
   path("logout",views.logout,name='logout'),
   path('cart/<int:pid>',views.add_to_cart,name ="add_to_cart"),
   path("find_total",views.total_price,name='total'),
   path("order_details",views.order_product,name='order_details'),
   path("remove_item/<int:pid>",views.remove_item,name='remove_item')
   

]