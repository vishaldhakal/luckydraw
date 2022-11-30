from django.contrib import admin
from django.urls import path
from .views import index, registerCustomer,deleteAllImeis,adminIndex,uploadIMEInos,indexWithError,downloadData,downloadDataToday,downloadDataYesterday,reuseIMEI

urlpatterns = [
    path('', index,name = 'index'),
    path('dashboard/', adminIndex,name = 'adminIndexx'),
    path('uploadimei/', uploadIMEInos,name = 'uploadimei'),
    path('delete-all-imei/', deleteAllImeis,name = 'deleteimeis'),
    path('', indexWithError,name = 'indexWithError'),
    path('output/', registerCustomer,name = 'register_customer'),
    path('export/', downloadData,name = 'down'),
    path('reuseimei/<str>/', reuseIMEI,name = 'reuseIMEI'),
    path('export-today/', downloadDataToday,name = 'down-today'),
    path('export-yesterday/', downloadDataYesterday,name = 'down-yest'),
]
