from django.contrib import admin
from .models import Room, Booking
from .models import Review


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('number', 'room_type')
    search_fields = ('number', 'room_type')
    list_filter = ('room_type','number')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('number','name', 'email', 'phone', 'room_type', 'check_in', 'check_out', 'no_of_rooms')
    search_fields = ('name', 'email', 'phone', 'room_type')
    list_filter = ('room_type', 'check_in', 'check_out')
    

@admin.register(Review)
class Reviewadmin(admin.ModelAdmin):
    list_display=['name','review','rating']




# Register your models here.
