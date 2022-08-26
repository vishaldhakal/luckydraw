from django.shortcuts import render, HttpResponse, redirect
from rest_framework.response import Response
from .models import Customer,Sales,Offers,Gift
from datetime import date


def index(request):
    return render(request, "index.html")

def indexWithError(request):
    ctx = {
        "error":"Invalid IMEI"
    }
    return render(request, "index.html",ctx)

def registerCustomer(request):
    if request.method == "POST":
        customer_name = request.POST["customer_name"]
        contact_number = request.POST["phone_number"]
        shop_name = request.POST["shop_name"]
        sold_area = request.POST["sold_area"]
        phone_model = request.POST["phone_model"]
        imei_number = request.POST["imei_number"]
        how_know_about_campaign = request.POST["how_know_about_campaign"]
        
        """ IMEI no check """

        get_all_customers = Customer.objects.all()

        for cust in get_all_customers:
            if cust.imei == imei_number:
                ctx = {
                "errormsg":"This IMEI no is already registered by customer "+cust.customer_name
                }
                return render(request, "index.html",ctx) 



        length_of_imei = len(imei_number)
        if(length_of_imei != 15 or imei_number[-2:]!="11"):
            ctx = {
                "errormsg":"Invalid IMEI no"
            }
            return render(request, "index.html",ctx) 

        customer = Customer.objects.create(customer_name=customer_name,phone_number=contact_number,shop_name=shop_name,sold_area=sold_area,phone_model=phone_model,sale_status="SOLD",imei=imei_number,how_know_about_campaign=how_know_about_campaign)
        customer.save()
        giftassign = False

        """ Select Gift """
        today_date = date.today()
        offers_all = Offers.objects.filter(date_valid=today_date)
        sales_all = Sales.objects.all()
        check = 0
        for sale in sales_all:
            if sale.date == today_date:
                check = 1
        if check == 0:
            saless = Sales.objects.create(sales_count=0,date=today_date)
            saless.save()
        
        sale_today = Sales.objects.get(date=today_date)
        get_sale_count = sale_today.sales_count
        sale_today.sales_count = get_sale_count+1
        sale_today.save()

        for offer in offers_all:
            if offer.type_of_offer == "After every certain sale":
                if (((get_sale_count+1)%offer.offer_condtion_value == 0)) and (offer.quantity > 0):
                    """ Grant Gift """
                    qty = offer.quantity
                    customer.gift = offer.gift
                    customer.save()
                    offer.quantity = qty-1;
                    offer.save()
                    giftassign = True
                    break
            else:
                if (get_sale_count+1  == offer.offer_condtion_value) and (offer.quantity > 0):
                    """ Grant Gift """
                    qty = offer.quantity
                    customer.gift = offer.gift
                    customer.save()
                    offer.quantity = qty-1;
                    offer.save()
                    giftassign = True
                    break
        return render(request, "output.html",{"customer":customer,"giftassigned":giftassign})
    else:
        return redirect('indexWithError')