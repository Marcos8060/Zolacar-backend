from django.db import models

# Create your models here.

class Car(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=30)
    price = models.CharField(max_length=10)
    luggage = models.CharField(max_length=20)
    doors = models.CharField(max_length=10)
    passengers = models.CharField(max_length=10)
    transmission = models.CharField(max_length=30)
    gas = models.CharField(max_length=30)
    interior1 = models.ImageField()
    interior2 = models.ImageField()
    interior3 = models.ImageField()

    def __str__(self):
        return self.name