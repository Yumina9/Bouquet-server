from django.db import models
from shops.models import Shop


class Ribbon(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to="image")
    price = models.IntegerField(default=0)
    shops = models.ForeignKey(Shop, on_delete=models.CASCADE)

    def __str__(self):
        return self.color + " " + self.name
