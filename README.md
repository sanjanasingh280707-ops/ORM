# Ex02 Django ORM Web Application
# Date: 20-11-2026
# AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

# DESIGN STEPS
## STEP 1:
Clone the problem from GitHub

## STEP 2:
Create a new app in Django project

## STEP 3:
Enter the code for admin.py and models.py

## STEP 4:
Execute Django admin and create details for 10 cars

# PROGRAM
....
admin.py

from django.contrib import admin
from .models import Zomato


class ZomatoAdmin(admin.ModelAdmin):
    list_display = ('food_name','restaurant_name','MobileNumber','price','Category','availability')

admin.site.register(Zomato,ZomatoAdmin)

models.py

from django.db import models

class Zomato(models.Model):
    food_name=models.CharField(max_length=20)
    restaurant_name=models.CharField(max_length=100)
    MobileNumber=models.CharField(max_length=15,default='00000000')
    price=models.IntegerField()
    Category=models.CharField(max_length=50)
    availability=models.BooleanField(default=True)
....
# OUTPUT




# RESULT
Thus the program for creating a database using ORM hass been executed successfully
