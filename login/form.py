from django import forms
from .models import Booking,Room
from .models import Review

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['number','name', 'email', 'phone', 'room_type', 'check_in', 'check_out', 'no_of_rooms']
        widgets = {
            'room_type': forms.Select(choices=Booking.ROOM_TYPES),
        }
class BookingRoom(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['number', 'room_type']
        widgets = {
            'room_type': forms.Select(choices=Booking.ROOM_TYPES),
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name','review', 'rating']





