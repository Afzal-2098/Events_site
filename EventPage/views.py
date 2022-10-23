from django.shortcuts import render
from . models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages


# Create your views here.
def Home(request):
    if request.method == "POST":
        event_name = request.POST.get('event_name')
        date = request.POST.get('date')
        time = request.POST.get('time')
        location = request.POST.get('location')
        image = request.FILES.get('image')
        event_data = Eventmodel(event_name = event_name, date = date, time = time, location = location, image = image)
        event_data.save()
        messages.add_message(request, messages.SUCCESS, "Event Uploded successfully.")
    return render(request, 'EventPage/base.html')


# User Registration view
def Register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            raise ValueError("Password Does not Match.")
        else:
            form_data = User(first_name = first_name, last_name = last_name, username = username, email = email, password = password1)
            form_data.save()
            messages.add_message(request, messages.SUCCESS, "registered successfully.")
    return render(request, 'EventPage/registration_form.html')


# User login view
def Login(request):
    username = request.POST.get('username')
    print(username)
    password = request.POST.get('password')
    print(password)
    user = authenticate(username=username, password=password)
    print(user)
    if user is not None:
        print(user)
        login(request, user)
        messages.add_message(request, messages.SUCCESS, "Logged in successfully.")
    return render(request, 'EventPage/login.html')


# events and view
def Event(request):
    events = reversed(Eventmodel.objects.all())
    if request.user.is_authenticated:
        if request.method == "POST":
            event_id = request.POST.get('eventname')
            # event = Eventmodel.objects.filter(id=event_id)
            likedevents = Liked_Event(user = request.user, event = event_id, is_liked = True)
            likedevents.save()
            messages.add_message(request, messages.INFO, "fas")
    return render(request, 'EventPage/event.html', {'events':events})
    

def LikedEvent(request):
    return render(request, 'EventPage/liked_event.html')