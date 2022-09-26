from django.urls import path
from .import views
urlpatterns = [
   path("viewseller",views.view_seller,name='viewseller'),

]