from django.contrib import admin
from .models import Zomato


class ZomatoAdmin(admin.ModelAdmin):
    list_display = ('food_name','restaurant_name','MobileNumber','price','Category','availability')

admin.site.register(Zomato,ZomatoAdmin)
