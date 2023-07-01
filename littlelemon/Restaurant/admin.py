from django.contrib import admin
from .models import Booking, Menu

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'bookingDate', 'no_of_guests')

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'inventory')