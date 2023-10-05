from django.db import models

# Create your models here.

class Menu(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    no_of_guests = models.IntegerField(null=True)
    booking_date = models.DateField(db_index=True)

class Booking(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, db_index=True)
    invenotry = models.IntegerField()


