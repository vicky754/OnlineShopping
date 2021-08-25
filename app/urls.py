from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    
    path('',home,name='home'),
    path('login/',loginview),
    #path('login/',loginview.as_view()),
    path('signup/',signup,name='signup'),
    path('product/<int:product_id>',productDetails,name='details'),
    path('logout/',signout),
]
   