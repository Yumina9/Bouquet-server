from django.db import models

class Shop(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='image', null=True, blank=True)
    location = models.CharField(max_length=200)
    florist = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    phone = models.CharField(max_length=50)
    instagram = models.CharField(max_length=100, null=True, blank=True)
    facebook = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.name