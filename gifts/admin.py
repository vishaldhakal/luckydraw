from django.contrib import admin
from .models import Customer, Gift,Offers,Sales

admin.site.register(Customer)
admin.site.register(Gift)
admin.site.register(Sales)
admin.site.register(Offers)