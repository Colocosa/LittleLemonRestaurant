from django.db import models

# Create your models here.
<<<<<<< HEAD
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guest = models.IntegerField()
    booking_date = models.DateTimeField()

    def __str__(self): 
        return self.name


# Add code to create Menu model
class Menu(models.Model):
   title = models.CharField(max_length=255) 
   price = models.DecimalField(max_digits=10, decimal_places=2) 
   inventory = models.IntegerField()

   def __str__(self):
       return f'{self.title} : {str(self.price)}'
   
   def get_item(self):
       return f'{self.title} : {str(self.price)}'
  
=======
# En el archivo models.py dentro de la carpeta de la aplicación Restaurant
class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()
    
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guest =models.IntegerField()
    bookingdata = models.DateTimeField()
>>>>>>> 158c1d284bef6649668e2917c87e124698bc6d72
