from django.db import models

# Create your models here.

class Booking(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    no_of_guests = models.IntegerField(null=True)
    booking_date = models.DateField(db_index=True)



class MenuItem(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, db_index=True)
    inventory = models.IntegerField()

    def get_item(self):
        return f'{self.title} : {str(self.price)}'
    
    def __str__(self):
        return str(self.title)

