from django.db import models

class Shop(models.Model):
    shop_name = models.CharField(max_length=50)
    shop_location = models.CharField(max_length=200)
    shop_florist = models.CharField(max_length=50)
    shop_description = models.CharField(max_length=300)
    shop_phone = models.CharField(max_length=50)
    shop_instagram = models.CharField(max_length=100)
    shop_facebook = models.CharField(max_length=100)
    
    def __str__(self):
        return self.shop_name