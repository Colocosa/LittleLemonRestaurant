from django.contrib import admin
<<<<<<< HEAD
from .models import *
# Register your models here.
=======
from restaurant.models import Booking, Menu
# Register your models here.

>>>>>>> 158c1d284bef6649668e2917c87e124698bc6d72
admin.site.register(Menu)
admin.site.register(Booking)