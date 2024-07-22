from django.shortcuts import render
# Create your views here.
from django.views.generic import ListView,DetailView

from .models import Gym , GymImages , Brand

class GymList(ListView):
    model = Gym

class GymDetails(DetailView):
    model = Gym