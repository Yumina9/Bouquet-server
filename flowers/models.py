from django.db import models

class Flower(models.Model):
    name= models.CharField(max_length=100)
    description =models.CharField(max_length=100)
    season = models.CharField(max_length=20)
    color = models.CharField(max_length=10)
    img = models.ImageField(upload_to="image")

    def __str__(self):
        return self.color + " "+self.name