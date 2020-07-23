from django.db import models

class Flower(models.Model):
    flower_name= models.CharField(max_length=100)
    flower_mean =models.CharField(max_length=100)
    flower_season = models.CharField(max_length=20)
    flower_color = models.CharField(max_length=10)

    def __str__(self):
        return self.flower_color + " "+self.flower_name