from django.db import models

class Zomato(models.Model):
    food_name=models.CharField(max_length=20)
    restaurant_name=models.CharField(max_length=100)
    MobileNumber=models.CharField(max_length=15,default='00000000')
    price=models.IntegerField()
    Category=models.CharField(max_length=50)
    availability=models.BooleanField(default=True)