from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Gym, GymImages, Brand

class GymList(ListView):
    model = Gym

class GymDetails(DetailView):
    model = Gym
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = GymImages.objects.filter(product=self.get_object())
        return context
