from django.db import models
from flowers.models import Flower
from ribbons.models import Ribbon
from wrappingPapers.models import WrappingPaper
from shops.models import Shop


class Bouquet(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    img = models.ImageField(upload_to='image')
    bouquet_paper_price = models.IntegerField(null=True, blank=True)
    flower = models.ManyToManyField(
        Flower, null=True, blank=True)
    ribbon = models.ManyToManyField(
        Ribbon, null=True, blank=True)
    wrappingpaper = models.ManyToManyField(
        WrappingPaper, null=True, blank=True)
    flower_count = models.IntegerField(null=True, blank=True)
    resultPrice = models.IntegerField(null=True, blank=True)
    shops = models.ForeignKey(
        Shop, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
