from django.contrib import admin
from .models import Customer, Gift,Offers,Sales,IMEINO,FixOffer

admin.site.register(Customer)
admin.site.register(Gift)
admin.site.register(Sales)
admin.site.register(Offers)
admin.site.register(IMEINO)
admin.site.register(FixOffer)