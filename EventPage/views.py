from django.shortcuts import render, redirect
from . models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
@login_required(login_url='/login/')
def Home(request):
    if request.method == "POST":
        event_name = request.POST.get('event_name')
        date = request.POST.get('date')
        time = request.POST.get('time')
        location = request.POST.get('location')
        image = request.FILES.get('image')
        event_data = Eventmodel(event_name = event_name, date = date, time = time, location = location, image = image)
        event_data.save()
        messages.add_message(request, messages.SUCCESS, "Event Has Been Uploaded Successfully.")
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
            user = User.objects.create_user(username=username, email=email, password=password1, first_name=first_name, last_name=last_name)
            user.save()
            if user is not None:
                login(request, user)
                messages.add_message(request, messages.SUCCESS, "registered successfully.")
    return render(request, 'EventPage/registration_form.html')


# User login view
def Login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request=request, username=username, password=password)
    if user is not None:
        login(request, user)
        messages.add_message(request, messages.SUCCESS, "You are Logged in Successfully.")
    return render(request, 'EventPage/login.html')


# User Logout view
def LogOut(request):
    logout(request)
    messages.success(request, "User Has been Logged Out.")
    # return render(request, "EventPage/login.html")
    return redirect("login")


# events and view
def Event(request):
    events = reversed(Eventmodel.objects.all())
    return render(request, 'EventPage/event.html', {'events':events})
    

def LikedEvent(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            event_id = request.POST.get('eventname')
            # event = Eventmodel.objects.filter(id=event_id)
            likedevents = Liked_Event(user = request.user, event = event_id, is_liked = True)
            likedevents.save()
            messages.add_message(request, messages.INFO, "fas")
    return render(request, 'EventPage/liked_event.html')