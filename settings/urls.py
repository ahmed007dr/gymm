from django.urls import path
from .views import home ,GymList , GymDetails 

urlpatterns = [
    path('',home),
    path('', GymList.as_view()),
    path('<slug:slug>', GymDetails.as_view()),
]
