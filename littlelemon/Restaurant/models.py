from django.db import models
from django.contrib.auth.models import User
class Booking(models.Model):
    name = models.CharField(max_length=255)
    bookingDate = models.DateField()
    no_of_guests = models.IntegerField(default=1)

    def __str__(self):
        return self.name

class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()

    def __str__(self):
       return f"{self.title} : {self.price}"

