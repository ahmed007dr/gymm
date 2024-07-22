from django.urls import path
from .views import GymList , GymDetails ,BrandList ,BrandDetails

urlpatterns = [
    path('', GymList.as_view()),
    path('<slug:slug>', GymDetails.as_view()),
    path('brands', BrandList.as_view()),
    path('brands/<slug:slug>', BrandDetails.as_view()),

]
