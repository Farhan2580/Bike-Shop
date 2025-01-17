from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField(default=0)
    price = models.FloatField(default=0.00)

    def __str__(self):
        return self.model


# Create your models here.
