from django.contrib import admin
from django.urls import path
from .views import index, registerCustomer,indexWithError,downloadData,downloadDataToday,uploadCustomer2,downloadDataYesterday


urlpatterns = [
    path('', index,name = 'index'),
    path('', indexWithError,name = 'indexWithError'),
    path('output/', registerCustomer,name = 'register_customer'),
    path('export/', downloadData,name = 'down'),
    path('uploaa/', uploadCustomer2,name = 'downsss'),
    path('export-today/', downloadDataToday,name = 'down-today'),
    path('export-yesterday/', downloadDataYesterday,name = 'down-yest'),
]
