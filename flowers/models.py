from django.db import models
from shops.models import Shop

class Flower(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    season = models.CharField(max_length=20)
    color = models.CharField(max_length=10)
    img = models.ImageField(upload_to="image")
    price = models.IntegerField(null=True, blank=True)
    shops = models.ForeignKey(
        Shop, on_delete=models.CASCADE,  null=True, blank=True)

    def __str__(self):
        return self.color + " "+self.name
