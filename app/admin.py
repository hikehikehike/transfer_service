from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from app.models import Car, Flight, Client

admin.site.register(Car)
admin.site.register(Flight)
admin.site.register(Client, UserAdmin)
