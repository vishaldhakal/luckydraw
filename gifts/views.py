from django.shortcuts import render, HttpResponse, redirect
from rest_framework.response import Response
from .models import Customer,Sales,Offers,Gift,IMEINO
from datetime import date, timedelta
import csv


def index(request):
    return render(request, "index.html")

def indexWithError(request):
    ctx = {
        "error":"Invalid IMEI"
    }
    return render(request, "index.html",ctx)

def uploadIMEI(request):
    imee = IMEINO.objects.all()
    imee.delete()
    with open('datas.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
        for row in data:
            okk = IMEINO.objects.create(imei_no=row[0])
            okk.save()
    ctx = {
        "error":"Invalid IMEI"
    }
    return render(request, "index.html",ctx)

def uploadCustomer2(request):
    custs = Customer.objects.all()
    custs.delete()
    with open('datas2.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
        for row in data:
            if(row[5]!=''):
                gifts = Gift.objects.get(name=row[5])
                customer = Customer.objects.create(customer_name=row[0],phone_number=row[3],shop_name=row[1],sold_area=row[2],phone_model=row[4],sale_status="SOLD",imei=row[6],how_know_about_campaign=row[8],date_of_purchase=row[7],gift=gifts)
                customer.save()
            else:
                customer = Customer.objects.create(customer_name=row[0],phone_number=row[3],shop_name=row[1],sold_area=row[2],phone_model=row[4],sale_status="SOLD",imei=row[6],how_know_about_campaign=row[8],date_of_purchase=row[7])
                customer.save()
            try:
                imeiii = IMEINO.objects.get(imei_no=row[6])
                imeiii.used = True
                imeiii.save()
            except:
                pass
    ctx = {
        "error":"Invalid IMEI"
    }
    return render(request, "index.html",ctx)

def downloadData(request):
    # Get all data from UserDetail Databse Table
    users = Customer.objects.all()

    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="all.csv"'

    writer = csv.writer(response)
    writer.writerow(['customer_name', 'shop_name', 'sold_area', 'phone_number','phone_model','gift','imei','date_of_purchase','how_know_about_campaign'])

    for user in users:
        if user.gift:
            writer.writerow([user.customer_name,user.shop_name,user.sold_area,user.phone_number,user.phone_model,user.gift.name,user.imei,user.date_of_purchase,user.how_know_about_campaign])
        else:
            writer.writerow([user.customer_name,user.shop_name,user.sold_area,user.phone_number,user.phone_model,user.gift,user.imei,user.date_of_purchase,user.how_know_about_campaign])
    return response

def downloadDataToday(request):
    # Get all data from UserDetail Databse Table
    today_date = date.today()
    users = Customer.objects.filter(date_of_purchase=today_date)

    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="today.csv"'

    writer = csv.writer(response)
    writer.writerow(['customer_name', 'shop_name', 'sold_area', 'phone_number','phone_model','gift','imei','date_of_purchase','how_know_about_campaign'])

    for user in users:
        if user.gift:
            writer.writerow([user.customer_name,user.shop_name,user.sold_area,user.phone_number,user.phone_model,user.gift.name,user.imei,user.date_of_purchase,user.how_know_about_campaign])
        else:
            writer.writerow([user.customer_name,user.shop_name,user.sold_area,user.phone_number,user.phone_model,user.gift,user.imei,user.date_of_purchase,user.how_know_about_campaign])
    return response

def downloadDataYesterday(request):
    # Get all data from UserDetail Databse Table
    today_date = date.today()- timedelta(days = 1)
    users = Customer.objects.filter(date_of_purchase=today_date)

    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="today.csv"'

    writer = csv.writer(response)
    writer.writerow(['customer_name', 'shop_name', 'sold_area', 'phone_number','phone_model','gift','imei','date_of_purchase','how_know_about_campaign'])

    for user in users:
        if user.gift:
            writer.writerow([user.customer_name,user.shop_name,user.sold_area,user.phone_number,user.phone_model,user.gift.name,user.imei,user.date_of_purchase,user.how_know_about_campaign])
        else:
            writer.writerow([user.customer_name,user.shop_name,user.sold_area,user.phone_number,user.phone_model,user.gift,user.imei,user.date_of_purchase,user.how_know_about_campaign])
    return response


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
        """ IMEI no check """

        get_all_customers = Customer.objects.all()

        for cust in get_all_customers:
            if cust.imei == imei_number:
                ctx = {
                "error":"This IMEI no is already registered by customer "+cust.customer_name
                }
                return render(request, "index.html",ctx) 
        
        imei_check=False
        get_all_imeis = IMEINO.objects.filter(used=False)
        for imeei in get_all_imeis:
            
            if imei_number==str(imeei):
                imei_check=True

        if(imei_check==False):
            ctx = {
                "error":"Invalid IMEI no entered"
            }
            return render(request, "index.html",ctx) 

        customer = Customer.objects.create(customer_name=customer_name,phone_number=contact_number,shop_name=shop_name,sold_area=sold_area,phone_model=phone_model,sale_status="SOLD",imei=imei_number,how_know_about_campaign=how_know_about_campaign)
        customer.save()
        imeiii = IMEINO.objects.get(imei_no=imei_number)
        imeiii.used = True
        imeiii.save()
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
                if (((get_sale_count)%offer.offer_condtion_value == 0)) and (offer.quantity > 0):
                    """ Grant Gift """
                    qty = offer.quantity
                    customer.gift = offer.gift
                    customer.save()
                    offer.quantity = qty-1;
                    offer.save()
                    giftassign = True
                    break
            else:
                if (get_sale_count  == offer.offer_condtion_value) and (offer.quantity > 0):
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