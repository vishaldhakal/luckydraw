from django.db import models

class Sales(models.Model):
   sales_count = models.IntegerField(default=0)
   date = models.DateField(auto_now=False,auto_created=False,auto_now_add=False)

   def __str__(self):
      return str(self.sales_count)

class Gift(models.Model):
   name = models.CharField(max_length=400)
   image_url = models.FileField()

   def __str__(self):
      return self.name

class IMEINO(models.Model):
   imei_no = models.CharField(max_length=400)
   used = models.BooleanField(default=False)

   def __str__(self):
      return self.imei_no

class FixOffer(models.Model):
   imei_no = models.CharField(max_length=400)
   quantity = models.IntegerField()
   gift = models.ForeignKey(Gift, on_delete=models.CASCADE)

   def __str__(self):
      return self.imei_no

class Offers(models.Model):

   OFFER_CHOICES = [
        ("After every certain sale", "After every certain sale"),
        ("At certain sale position", "At certain sale position"),
      ]

   gift = models.ForeignKey(Gift, on_delete=models.CASCADE)
   date_valid= models.DateField(auto_now_add=False,auto_now=False)
   quantity = models.IntegerField()
   type_of_offer = models.CharField(max_length=800, choices=OFFER_CHOICES)
   offer_condtion_value = models.IntegerField()
   
   def __str__(self):
      return "Offer on "+self.gift.name

class Customer(models.Model):

   CAMPAIGN_CHOICES = [
        ("Facebook Ads", "Facebook Ads"),
        ("Reatil Shop", "Reatil Shop"),
        ("Google Ads", "Google Ads"),
        ("Others", "Others"),
      ]

   customer_name = models.CharField(max_length=400)
   shop_name = models.TextField()
   sold_area = models.CharField(max_length=800)
   phone_number = models.CharField(max_length=400)
   phone_model = models.CharField(max_length=400)
   sale_status = models.CharField(max_length=400,default="SOLD")
   prize_details = models.CharField(max_length=900,default="Happy Sales Carnival")
   gift = models.ForeignKey(Gift, on_delete=models.CASCADE,null=True)
   imei = models.CharField(max_length=400)
   date_of_purchase = models.DateField(auto_now_add=True, auto_now=False)
   how_know_about_campaign = models.CharField(max_length=800, choices=CAMPAIGN_CHOICES)

   def __str__(self):
      return self.customer_name

   class Meta:
        ordering = ("-date_of_purchase",)