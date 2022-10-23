from socket import fromshare
from time import time
from django import forms

class EventForm(forms.Form):
    event_name = forms.CharField(max_length = 100)
    date = forms.DateField()
    time = forms.DateField()
    location = forms.CharField(max_length = 120)
    image = forms.ImageField()
    