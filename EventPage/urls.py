from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('events/', views.Event, name='event'),
    path('user-register/', views.Register, name='register'),
    path('login/', views.Login, name='login'),
    path('liked-events/', views.LikedEvent, name='liked-events'),
    
]
