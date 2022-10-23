import imp
from pyexpat import model
from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Eventmodel)
class EventmodelModelAdmin(admin.ModelAdmin):
        list_display = ['id', 'event_name', 'date', 'time', 'location', 'image',]

@admin.register(Liked_Event)
class Liked_EventModelAdmin(admin.ModelAdmin):
        list_display = ['id', 'user', 'event', 'is_liked']