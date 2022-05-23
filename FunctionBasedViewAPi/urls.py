from django.urls import path
from .views import FunctionBasedCRUDApi

urlpatterns = [
    path('api/', FunctionBasedCRUDApi),
]