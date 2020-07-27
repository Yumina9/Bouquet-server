from django.db import models

class Bouquet(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    img = models.ImageField(upload_to='image')

    def __str__(self):
        return self.name