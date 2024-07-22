from django.urls import path
from .views import GymList , GymDetails

urlpatterns = [
    path('', GymList.as_view()),
    path('<slug:slug>', GymDetails.as_view())

]
