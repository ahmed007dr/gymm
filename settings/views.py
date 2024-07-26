from django.shortcuts import render

from django.views.generic import ListView, DetailView
from products.models import Gym, GymImages
# Create your views here.


def home(request):
    return render(request,'settings/home.html',{})

class GymList(ListView):
    model = Gym
    template_name = 'settings/home.html'  
    context_object_name = 'object_list'


class GymDetails(DetailView):
    model = Gym
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = GymImages.objects.filter(product=self.get_object())
        return context