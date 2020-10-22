from django.db import models
from shops.models import Shop
from users.models import User
from bouquets.models import Bouquet
from flowers.models import Flower

class Bouquet_order(models.Model):

    shops = models.ForeignKey(
        Shop, on_delete=models.CASCADE, blank=True)

    users = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True)

    bouquet = models.ForeignKey(Bouquet, on_delete=models.CASCADE, null=True)
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE, null=True)

    flower_count = models.IntegerField(default=1)
    ribbon = models.CharField(max_length=100, blank=True)
    wrappingPaper = models.CharField(max_length=100, blank=True)
    price = models.IntegerField(default=0)
