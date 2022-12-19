from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from app.models import Car, Trip, Client

admin.site.register(Car)
admin.site.register(Trip)


@admin.register(Client)
class ClientAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("phone_number",)
    fieldsets = UserAdmin.fieldsets + (
        (("Additional info", {"fields": ("phone_number",)}),)
    )
