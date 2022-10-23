from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Eventmodel(models.Model):
    event_name = models.CharField(max_length = 100)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length = 120)
    image = models.ImageField(upload_to ='img')

class Liked_Event(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    event = models.CharField(max_length=20)
    is_liked = models.BooleanField(default = False)
    