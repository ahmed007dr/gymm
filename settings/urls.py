from django.urls import path
from .views import home ,GymList , GymDetails 

urlpatterns = [
    path('',home),
]
