from django.contrib import admin
from django.urls import path
from .views import index, registerCustomer,adminIndex,indexWithError,downloadData,downloadDataToday,downloadDataYesterday,reuseIMEI

urlpatterns = [
    path('', index,name = 'index'),
    path('dashboard/', adminIndex,name = 'adminIndex'),
    path('', indexWithError,name = 'indexWithError'),
    path('output/', registerCustomer,name = 'register_customer'),
    path('export/', downloadData,name = 'down'),
    path('reuseimei/<str>/', reuseIMEI,name = 'reuseIMEI'),
    path('export-today/', downloadDataToday,name = 'down-today'),
    path('export-yesterday/', downloadDataYesterday,name = 'down-yest'),
]
