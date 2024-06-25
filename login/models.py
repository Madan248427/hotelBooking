
from django.db import models

class users(models.Model):
    name=models.CharField(max_length=125)
    email=models.EmailField()
    password=models.CharField(max_length=92)
    def __str__(self):
        return str(self.id)
   
        


    


class Room(models.Model):
    ROOM_TYPES = (
        ('single', 'Single Room'),
        ('double', 'Double Room'),
        ('suite', 'Suite'),
    )
    number = models.CharField(max_length=10, unique=True)
    room_type = models.CharField(max_length=10, choices=ROOM_TYPES)
    #price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.get_room_type_display()} - Room {self.number}'

class Booking(models.Model):
    ROOM_TYPES = (
        ('single', 'Single Room'),
        ('double', 'Double Room'),
        ('suite', 'Suite'),
    )
   
    name = models.CharField(max_length=100,null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=15,null=True)
    room_type = models.CharField(max_length=10, choices=ROOM_TYPES,null=True)
    check_in = models.DateField(null=True)
    check_out = models.DateField(null=True)
    no_of_rooms = models.PositiveIntegerField(null=True)
    number = models.CharField(max_length=10, unique=True,null=True)


class Review(models.Model):
    
    name=models.CharField(max_length=30,null=True,blank=True)
    
    review=models.TextField(max_length=1000)
    rating=models.IntegerField()

    def __str__(self):
        return str(self.id)













# Create your models here.
