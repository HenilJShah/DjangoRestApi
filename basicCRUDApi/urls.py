from django.urls import path
from .views import createStudent

urlpatterns = [
    path('create/', createStudent),   
]