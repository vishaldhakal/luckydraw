from django.contrib import admin
from django.urls import path
from .views import index, registerCustomer,indexWithError,uploadIMEI


urlpatterns = [
    path('', index,name = 'index'),
    path('', indexWithError,name = 'indexWithError'),
    path('output/', registerCustomer,name = 'register_customer'),
    path('upload/', uploadIMEI,name = 'upload_imei'),
]
